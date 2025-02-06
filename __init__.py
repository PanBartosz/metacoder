from flask_migrate import Migrate
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, request, url_for, abort, flash, send_file, jsonify
from flask_ckeditor import CKEditor
from flask_uploads import configure_uploads, IMAGES, UploadSet
from sqlalchemy import inspect
import yaml

import os
import pandas as pd
import uuid
BASE_PATH = os.getenv('BASE_PATH')
with open(BASE_PATH + "/translations.yaml", "r") as f:
    t = yaml.safe_load(f)

# Flask

def get_header(q):
    return t["q"][q]["head"]
def get_forcoders(q):
    return t["q"][q]["forcoders"]
def get_text(q):
    return t["q"][q]["text"]


# Komponenty aplikacji

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'trudnytajnyklucz'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + BASE_PATH + '/baza.db'
UPLOAD_FOLDER = BASE_PATH + '/media/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOADED_PHOTOS_DEST'] = 'media/images'  # Destination for uploaded images
app.config['PREFERRED_URL_SCHEME'] = 'https'
app.jinja_env.add_extension('jinja_markdown.MarkdownExtension')
app.jinja_env.filters['header'] = get_header
app.jinja_env.filters['text'] = get_text
app.jinja_env.filters['forcoders'] = get_forcoders


db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)


# czy to nie działało, bo w złej kolejności to robiłem? chyba tak...
ckeditor = CKEditor(app)
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['CKEDITOR_HEIGHT'] = 600
app.config['CKEDITOR_EXTRA_PLUGINS'] = ['filebrowser']



#app.config['CKEDITOR_ENABLE_CSRF'] = True


from .forms import LoginForm, RegistrationForm, ArticleForm, CreateArticleForm, DeleteForm
from .models import User, Article, ArticlePermission

# Komponenty aplikacji

# Main page

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CreateArticleForm()
    available_articles = Article.query.all()
    return render_template('index.html', form=form,
                           available_articles=available_articles)

# Login and registration


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role="user")
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/createnew', methods=['GET', 'POST'])
def createnew():
    if not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = CreateArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        article = Article(short=form.short.data, author=current_user)
        db.session.add(article)
        db.session.commit()
        current_user.add_permissions(article.id, ["view", "edit", "delete"])
    return redirect(url_for('index'))

@app.route('/edit', methods=["GET", "POST"])
def edit():
    if request.method == 'GET':
        article = Article.query.get(request.args.get("id"))
        if not current_user.can_edit(article.id):
            return "Cannot edit this article!"
        form = ArticleForm(obj=article)
        return render_template("viewedit.html", form=form, mode = "edit", t = t,
                               get_forcoders = get_forcoders, get_header = get_header, get_text = get_text)
    if request.method == 'POST':
        form = ArticleForm(request.form)
        if not current_user.can_edit(form.id.data):
            return "Cannot edit this article!"
        if form.validate() or True: # Tutaj coś się zepsuło a może nigdy nie działało
            article = Article.query.get(form.id.data)
            form.populate_obj(article)
            db.session.commit()
        else:
            print(form.errors)
        return render_template("viewedit.html", form=form, mode = "edit", t = t, get_forcoders = get_forcoders, get_header = get_header, get_text = get_text)

@app.route('/print', methods=["GET", "POST"])
def _print():
    if request.method == 'GET':
        article = Article.query.get(request.args.get("id"))
        if not current_user.can_edit(article.id):
            return "Cannot edit this article!"
        form = ArticleForm(obj=article)
        return render_template("viewedit.html", form=form, mode = "view", printable = True, t = t, get_forcoders = get_forcoders, get_header = get_header, get_text = get_text)
    if request.method == 'POST':
        return("Something went wrong")

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if request.method == 'GET':
        article = Article.query.get(request.args.get("id"))
        form = DeleteForm(obj=article)
        return render_template("delete.html", form=form)
    if request.method == 'POST':
        form = DeleteForm(request.form)
        if form.confirm.data == "YES":
            article = Article.query.filter(Article.id == form.id.data).delete()
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))


@app.route('/view', methods=["GET", "POST"])
def view():
    if request.method == 'GET':
        article = Article.query.get(request.args.get("id"))
        if not current_user.can_edit(article.id):
            return "Cannot edit this article!"
        form = ArticleForm(obj=article)
        return render_template("viewedit.html", form=form, mode = "view", t = t, get_forcoders = get_forcoders, get_header = get_header, get_text = get_text)
    if request.method == 'POST':
        return("Something went wrong")

        
@app.route('/upload', methods=['POST'])
def upload():
    if 'upload' in request.files:
        filename = photos.save(request.files['upload'])
        url = photos.url(filename)
        return jsonify(uploaded=1, fileName=filename, url=url)
        return f"<script type='text/javascript'>window.parent.CKEDITOR.tools.callFunction(1, '{url}', '')</script>"
    return 'Failed to upload image', 400


@app.route('/export', methods=['POST'])
def export_responses():
    data = request.get_json()
    if not data or 'ids' not in data:
        return jsonify({"error": "No 'ids' provided"}), 400
    ids = [int(i) for i in data['ids']]
    articles = Article.query.filter(Article.id.in_(ids)).all()
    permitted_articles = [
        article for article in articles 
        if current_user.can_view(article.id)
    ]
    if not permitted_articles:
        return jsonify({"error": "No articles found or no permission"}), 403

    article_columns = [col.key for col in inspect(Article).attrs if hasattr(col, 'columns')]

    # Convert article objects into list of dicts,
    # so pandas can transform them into a DataFrame.
    data_list = []
    for article in permitted_articles:
        row_data = {}
        for col_name in article_columns:
            # Use getattr to fetch each column's value from the Article instance
            row_data[col_name] = getattr(article, col_name)
        data_list.append(row_data)

    # 5. Create a pandas DataFrame and export it as an Excel file
    df = pd.DataFrame(data_list, columns=article_columns)
    export_folder = os.path.join(BASE_PATH, 'static', 'exports')
    os.makedirs(export_folder, exist_ok=True)

    file_id = str(uuid.uuid4())
    file_name = f"export_{file_id}.xlsx"

    export_path = os.path.join(export_folder, file_name)
    df.to_excel(export_path, index=False)

    file_url = url_for('static', filename=f'exports/{file_name}', _external=True, _scheme = "https")
    return jsonify({"url": file_url}), 200


def compare_xlsx_columns(df, translations):
    excluded_columns = ["created_date", "modified_date", "id", "short", "recruitment1a"]
    cols_to_check = [
        col for col in df.columns 
        if not col.endswith("_e") 
        and not col.endswith("_comment") 
        and col not in excluded_columns
    ]

    agreement_counter = 0
    disagreement_counter = 0
    differences_data = []

    for col in cols_to_check:
        unique_vals = df[col].unique()

        # If there's more than one unique value, store differences
        print(col)
        print(unique_vals)
        if len(unique_vals == 1) and unique_vals[0] == "":
            continue
        if len(unique_vals) > 1:
            disagreement_counter += 1
            col_diffs = {
                "column_name": col,
                "column_title": translations["q"][col]["head"].strip("#").strip() 
                                if col in translations["q"] else col,
                "rows": []
            }
            for idx, row in df.iterrows():
                short_val = row["short"] if "short" in df.columns else "N/A"
                col_val = row[col]
                # Attempt to look up a friendly "choice" name
                try:
                    choices = translations["q"][col]["choices"]
                    choice_name = [
                        choice[1] for choice in choices 
                        if choice[0] == col_val
                    ][0]
                except:
                    choice_name = str(col_val)

                col_diffs["rows"].append({
                    "row_index": idx,
                    "short": short_val,
                    "value": choice_name
                })

            differences_data.append(col_diffs)
        else:
            agreement_counter += 1

    return {
        "differences": differences_data,
        "agreement_count": agreement_counter,
        "disagreement_count": disagreement_counter,
        "total": agreement_counter + disagreement_counter
    }

@app.route("/compare", methods=["GET", "POST"])
def compare():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part in request", 400

        file = request.files["file"]

        if file.filename == "":
            return "No selected file", 400

        try:
            df = pd.read_excel(file, na_values=[], keep_default_na=False)
        except Exception as e:
            return f"Error reading Excel file: {e}", 400

        results = compare_xlsx_columns(df, t)

        return render_template("results.html", results=results)

    return render_template("upload_form.html")
