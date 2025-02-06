from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy.sql import func

from . import db, login

from datetime import datetime
from datetime import UTC


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(120), nullable=True)
    password_hash = db.Column(db.String(128))

    article_permissions = db.relationship(
        'ArticlePermission', cascade='all, delete')
    articles = db.relationship("Article", back_populates='author')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def can_edit(self, article_id):
        if self.role == "admin":
            return True
        return True if ArticlePermission.query.filter(ArticlePermission.user_id == self.id,
                                                       ArticlePermission.article_id == article_id,
                                                     ArticlePermission.permission == "edit").all() else False

    def can_delete(self, article_id):
        if self.role == "admin":
            return True
        if ArticlePermission.query.filter(ArticlePermission.user_id == self.id,
                                          ArticlePermission.article_id == article_id,

                                          ArticlePermission.permission == "delete").all():
            return True

    def can_view(self, article_id):
        if self.role == "admin":
            return True
        if ArticlePermission.query.filter(ArticlePermission.user_id == self.id,
                                          ArticlePermission.article_id == article_id,
                                          ArticlePermission.permission == "view").all():
            return True

    def add_permissions(self, article_id, permissions):
        for perm in permissions:
            p = ArticlePermission(user_id=self.id,
                                  article_id=article_id,
                                  permission=perm
                                  )
            db.session.add(p)
            db.session.commit()


class ArticlePermission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey(
        'article.id'), nullable=False)

    permission = db.Column(db.String(200), unique=False, nullable=False)
    user = db.relationship('User', lazy=True)
    Article = db.relationship('Article', lazy=True)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(200))
    onlinefirst = db.Column(db.Integer)
    n_studies = db.Column(db.Integer)
    first_study = db.Column(db.String(200))
    # Transparency
    open_access = db.Column(db.String(200))
    open_access_e = db.Column(db.String)
    preregistration = db.Column(db.String(200))
    preregistration_e = db.Column(db.String)
    statement_of_availability = db.Column(db.String(200))
    statement_of_availability_e = db.Column(db.String)
    materials_availability = db.Column(db.String(200))
    materials_availability_e = db.Column(db.String)
    data_availability = db.Column(db.String(200))
    data_availability_e = db.Column(db.String)
    code_availability = db.Column(db.String(200))
    code_availability_e = db.Column(db.String)
    general_comment = db.Column(db.String)
    transparency_comment = db.Column(db.String)
    methods_comment = db.Column(db.String)
    methodsq_comment = db.Column(db.String)
    methodsnq_comment = db.Column(db.String)
    results_comment = db.Column(db.String)
    conclusions_comment = db.Column(db.String)
    # Methods
    background1 = db.Column(db.String(200))
    background1_e = db.Column(db.String)
    background2 = db.Column(db.String(200))
    background2_e = db.Column(db.String)
    background3 = db.Column(db.String(200))
    background3_e = db.Column(db.String)
    background4 = db.Column(db.String(200))
    background4_e = db.Column(db.String)

    goals1 = db.Column(db.String(200))
    goals1_e = db.Column(db.String)
    goals2 = db.Column(db.String(200))
    goals2_e = db.Column(db.String)
    goals3 = db.Column(db.String(200))
    goals3_e = db.Column(db.String)

    conceptual1 = db.Column(db.String(200))
    conceptual1_e = db.Column(db.String)
    conceptual2 = db.Column(db.String(200))
    conceptual2_e = db.Column(db.String)
    conceptual3 = db.Column(db.String(200))
    conceptual3_e = db.Column(db.String)

    recruitment1 = db.Column(db.String(200))
    recruitment1_e = db.Column(db.String)
    recruitment1a = db.Column(db.String(200))
    recruitment1a_e = db.Column(db.String)
    recruitment2 = db.Column(db.String(200))
    recruitment2_e = db.Column(db.String)
    recruitment3 = db.Column(db.String(200))
    recruitment3_e = db.Column(db.String)

    incentives = db.Column(db.String(200))
    incentives_e = db.Column(db.String)
    participants1 = db.Column(db.String(200))
    participants1_e = db.Column(db.String)
    participants2 = db.Column(db.String(200))
    participants2_e = db.Column(db.String)
    participants3 = db.Column(db.String(200))
    participants3_e = db.Column(db.String)
    participants4 = db.Column(db.String(200))
    participants4_e = db.Column(db.String)
    participants5 = db.Column(db.String(200))
    participants5_e = db.Column(db.String)

    exclusion0 = db.Column(db.String(200))
    exclusion0_e = db.Column(db.String)
    exclusion1 = db.Column(db.String(200))
    exclusion1_e = db.Column(db.String)
    exclusion2 = db.Column(db.String(200))
    exclusion2_e = db.Column(db.String)

    exclumeasure1 = db.Column(db.String(200))
    exclumeasure1_e = db.Column(db.String)
    exclumeasure2 = db.Column(db.String(200))
    exclumeasure2_e = db.Column(db.String)
    exclumeasure3 = db.Column(db.String(200))
    exclumeasure3_e = db.Column(db.String)

    kindofstudy = db.Column(db.String(200))
    statistical_analysis = db.Column(db.String(200))
    statistical_analysis_e = db.Column(db.String)

    nqmeasure1 = db.Column(db.String(200))
    nqmeasure1_e = db.Column(db.String)
    nqmeasure2 = db.Column(db.String(200))
    nqmeasure2_e = db.Column(db.String)
    nqmeasure3 = db.Column(db.String(200))
    nqmeasure3_e = db.Column(db.String)
    nqmeasure4 = db.Column(db.String(200))
    nqmeasure4_e = db.Column(db.String)
    nqmeasure5 = db.Column(db.String(200))
    nqmeasure5_e = db.Column(db.String)
    nqmeasure6 = db.Column(db.String(200))
    nqmeasure6_e = db.Column(db.String)
    nqmeasure7 = db.Column(db.String(200))
    nqmeasure7_e = db.Column(db.String)
    nqmeasure8 = db.Column(db.String(200))
    nqmeasure8_e = db.Column(db.String)
    nqmeasure9 = db.Column(db.String(200))
    nqmeasure9_e = db.Column(db.String)
    nqmeasure10 = db.Column(db.String(200))
    nqmeasure10_e = db.Column(db.String)
    nqmeasure11 = db.Column(db.String(200))
    nqmeasure11_e = db.Column(db.String)
    nqmeasure11a = db.Column(db.String(200))
    nqmeasure11a_e = db.Column(db.String)
    nqmeasure11b = db.Column(db.String(200))
    nqmeasure11b_e = db.Column(db.String)
    nqmeasure11c = db.Column(db.String(200))
    nqmeasure11c_e = db.Column(db.String)
    nqmeasure11d = db.Column(db.String(200))
    nqmeasure11d_e = db.Column(db.String)
    nqmeasure11e = db.Column(db.String(200))
    nqmeasure11e_e = db.Column(db.String)
    nqmeasure12 = db.Column(db.String(200))
    nqmeasure12_e = db.Column(db.String)
    nqmeasure13 = db.Column(db.String(200))
    nqmeasure13_e = db.Column(db.String)
    nqmeasure14 = db.Column(db.String(200))
    nqmeasure14_e = db.Column(db.String)
    nqmeasure15 = db.Column(db.String(200))
    nqmeasure15_e = db.Column(db.String)
    nqmeasure16 = db.Column(db.String(200))
    nqmeasure16_e = db.Column(db.String)
    nqmeasure17 = db.Column(db.String(200))
    nqmeasure17_e = db.Column(db.String)
    nqmeasure18 = db.Column(db.String(200))
    nqmeasure18_e = db.Column(db.String)

    qmeasure1 = db.Column(db.String(200))
    qmeasure1_e = db.Column(db.String)
    qmeasure2 = db.Column(db.String(200))
    qmeasure2_e = db.Column(db.String)
    qmeasure3 = db.Column(db.String(200))
    qmeasure3_e = db.Column(db.String)
    qmeasure4 = db.Column(db.String(200))
    qmeasure4_e = db.Column(db.String)
    qmeasure5 = db.Column(db.String(200))
    qmeasure5_e = db.Column(db.String)
    qmeasure6 = db.Column(db.String(200))
    qmeasure6_e = db.Column(db.String)
    qmeasure6a = db.Column(db.String(200))
    qmeasure6a_e = db.Column(db.String)
    qmeasure6b = db.Column(db.String(200))
    qmeasure6b_e = db.Column(db.String)
    qmeasure6c = db.Column(db.String(200))
    qmeasure6c_e = db.Column(db.String)
    qmeasure6d = db.Column(db.String(200))
    qmeasure6d_e = db.Column(db.String)
    qmeasure6e = db.Column(db.String(200))
    qmeasure6e_e = db.Column(db.String)
    qmeasure6f  = db.Column(db.String(200))
    qmeasure6f_e  = db.Column(db.String)
    qmeasure7a  = db.Column(db.String(200))
    qmeasure7a_e  = db.Column(db.String)
    qmeasure7b  = db.Column(db.String(200))
    qmeasure7b_e  = db.Column(db.String)
    qmeasure7c  = db.Column(db.String(200))
    qmeasure7c_e  = db.Column(db.String)
    qmeasure7d  = db.Column(db.String(200))
    qmeasure7d_e  = db.Column(db.String)
    qmeasure8  = db.Column(db.String(200))
    qmeasure8_e  = db.Column(db.String)
    qmeasure9  = db.Column(db.String(200))
    qmeasure9_e  = db.Column(db.String)
    qmeasure10  = db.Column(db.String(200))
    qmeasure10_e  = db.Column(db.String)

    flow1  = db.Column(db.String(200))
    flow1_e  = db.Column(db.String)
    flow2  = db.Column(db.String(200))
    flow2_e  = db.Column(db.String)
    flow3  = db.Column(db.String(200))
    flow3_e  = db.Column(db.String)

    descriptive1  = db.Column(db.String(200))
    descriptive1_e  = db.Column(db.String)
    descriptive2  = db.Column(db.String(200))
    descriptive2_e  = db.Column(db.String)

    inferential1  = db.Column(db.String(200))
    inferential1_e  = db.Column(db.String)
    inferential2  = db.Column(db.String(200))
    inferential2_e  = db.Column(db.String)
    inferential3  = db.Column(db.String(200))
    inferential3_e  = db.Column(db.String)

    interpretation  = db.Column(db.String(200))
    interpretation_e  = db.Column(db.String)
    validity  = db.Column(db.Integer)
    validity_e  = db.Column(db.String)

    # Bookkeeping
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('User', back_populates='articles')
    created_date = db.Column(db.DateTime, nullable=True,
                             default=datetime.now(UTC))
    modified_date = db.Column(
        db.DateTime, nullable=True, default=datetime.now(UTC), onupdate=datetime.now)
    permissions = db.relationship('ArticlePermission', cascade='all, delete')
