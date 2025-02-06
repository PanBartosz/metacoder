from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, SubmitField, RadioField, PasswordField, BooleanField, SelectMultipleField, FieldList, IntegerField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, DataRequired, Email, EqualTo
from flask_ckeditor import CKEditorField
import os

from .models import User
import yaml

BASE_PATH = os.getenv('BASE_PATH')
with open(BASE_PATH + "/translations.yaml", "r") as f:
    t = yaml.safe_load(f)

def get_choices(question):
    return t["q"][question]["choices"]

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-mail is already taken')


# Common option sets:
yesno = [("Y", "a. yes"), ("N", "b. no")]
yesnona = [("Y", "a. yes"), ("N", "b. no"), ("NA", "c. not applicable")]
yespno = [("Y", "a. yes"), ("P", "b. partly"), ("N", "c. no")]


class ArticleForm(FlaskForm):
    id = HiddenField('Id')

    # General
    short = StringField('Short')
    title = StringField('Title')
    onlinefirst = StringField("onlinefirst")
    n_studies = StringField("N_studies")
    first_study = StringField("First_study")
    general_comment = CKEditorField("general_comment")

    # Transparency
    open_access = RadioField("Open_access",
                             choices= get_choices("open_access"))
    open_access_e = CKEditorField("open_access_e")

    preregistration = RadioField("Preregistration",
                                 choices=get_choices("preregistration"))

    preregistration_e = CKEditorField("preregistration_e")

    statement_of_availability = RadioField("Statement_of_availability",
                                           choices=get_choices("statement_of_availability"))

    statement_of_availability_e = CKEditorField("preregistration_e")

    materials_availability = RadioField("materials_availability",
                                        choices=get_choices("materials_availability"))
    materials_availability_e = CKEditorField("materials_availability_e")

    data_availability = RadioField("data_availability",
                                   choices= get_choices("data_availability")
                                   )
    data_availability_e = CKEditorField("data_availability_e")

    code_availability = RadioField("code_availability",
                                   choices=get_choices("code_availability"))
    code_availability_e = CKEditorField("code_availability_e")
    transparency_comment = CKEditorField("transparency_comment")
    
    # Methods 
    background1 = RadioField("background1",
                             choices=get_choices("background1"))
    background1_e = CKEditorField("background1_e")
    background2 = RadioField("background2",
                             choices=get_choices("background2"))
    background2_e = CKEditorField("background2_e")
    background3 = RadioField("background3",
                             choices=get_choices("background3"))
    background3_e = CKEditorField("background3_e")
    background4 = RadioField("background4",
                             choices=get_choices("background4"))
    background4_e = CKEditorField("background4_e")

    goals1 = RadioField("goals1", choices=get_choices("goals1"))
    goals1_e = CKEditorField("goals1_e")
    goals2 = RadioField("goals1", choices=get_choices("goals2"))
    goals2_e = CKEditorField("goals2_e")
    goals3 = RadioField("goals1", choices=get_choices("goals3"))
    goals3_e = CKEditorField("goals3_e")

    conceptual1 = RadioField("conceptual1", choices=get_choices("conceptual1"))
    conceptual1_e = CKEditorField("conceptual1_e")
    conceptual2 = RadioField("conceptual2", choices=get_choices("conceptual2"))
    conceptual2_e = CKEditorField("conceptual2_e")
    conceptual3 = RadioField("conceptual3", choices=get_choices("conceptual3"))
    conceptual3_e = CKEditorField("conceptual3_e")

    recruitment1 = RadioField("recruitment1", choices=get_choices("recruitment1"))
    recruitment1_e = CKEditorField("recruitment1_e")
    recruitment1a = StringField("recruitment1a")
    recruitment1a_e = CKEditorField("recruitment1a_e")
    recruitment2 = RadioField("recruitment2", choices=get_choices("recruitment2"))
    recruitment2_e = CKEditorField("recruitment2_e")
    recruitment3 = RadioField("recruitment3", choices=get_choices("recruitment3"))
    recruitment3_e = CKEditorField("recruitment3_e")

    incentives = RadioField("incentives", choices=get_choices("incentives"))
    incentives_e = CKEditorField("incentives_e")

    participants1 = RadioField("participants1", choices=get_choices("participants1"))
    participants1_e = CKEditorField("participants1_e")
    participants2 = RadioField("participants2", choices=get_choices("participants2"))
    participants2_e = CKEditorField("participants3_e")
    participants3 = RadioField("participants3", choices=get_choices("participants3"))
    participants3_e = CKEditorField("participants3_e")
    participants4 = RadioField("participants4", choices=get_choices("participants4"))
    participants4_e = CKEditorField("participants4_e")
    participants5 = RadioField("participants5", choices=get_choices("participants5"))
    participants5_e = CKEditorField("participants5_e")

    exclusion0 = RadioField("exclusion0", choices=get_choices("exclusion0"))
    exclusion0_e = CKEditorField("exclusion0_e")
    exclusion1 = RadioField("exclusion1", choices=get_choices("exclusion1"))
    exclusion1_e = CKEditorField("exclusion1_e")
    exclusion2 = RadioField("exclusion2", choices=get_choices("exclusion2"))
    exclusion2_e = CKEditorField("exclusion2_e")

    exclumeasure1 = RadioField("exclumeasure1", choices=get_choices("exclumeasure1"))
    exclumeasure1_e = CKEditorField("exclumeasure1_e")
    exclumeasure2 = RadioField("exclumeasure2", choices=get_choices("exclumeasure2"))
    exclumeasure2_e = CKEditorField("exclumeasure2_e")
    exclumeasure3 = RadioField("exclumeasure3", choices=get_choices("exclumeasure3"))
    exclumeasure3_e = CKEditorField("exclumeasure3_e")

    kindofstudy = RadioField("kindofstudy", choices=get_choices("kindofstudy"))

    statistical_analysis = RadioField("statistica_analysis",
                                      choices=get_choices("statistical_analysis"))
    statistical_analysis_e = CKEditorField("statistical_analysis_e")
    methods_comment = CKEditorField("methods_comment")

    # Methods (non-questionnaire)
    nqmeasure1 = RadioField("nqmeasure1", choices=get_choices("nqmeasure1"))
    nqmeasure1_e = CKEditorField("nqmeasure1_e")
    nqmeasure2 = RadioField("nqmeasure2", choices=get_choices("nqmeasure2"))
    nqmeasure2_e = CKEditorField("nqmeasure2_e")
    nqmeasure3 = RadioField("nqmeasure3", choices=get_choices("nqmeasure3"))
    nqmeasure3_e = CKEditorField("nqmeasure3_e")
    nqmeasure4 = RadioField("nqmeasure4", choices=get_choices("nqmeasure4"))
    nqmeasure4_e = CKEditorField("nqmeasure4_e")
    nqmeasure5 = RadioField("nqmeasure5", choices=get_choices("nqmeasure5"))
    nqmeasure5_e = CKEditorField("nqmeasure5_e")
    nqmeasure6 = RadioField("nqmeasure6", choices=get_choices("nqmeasure6"))
    nqmeasure6_e = CKEditorField("nqmeasure6_e")
    nqmeasure7 = RadioField("nqmeasure6", choices=get_choices("nqmeasure7"))
    nqmeasure7_e = CKEditorField("nqmeasure7_e")
    nqmeasure8 = RadioField("nqmeasure8", choices=get_choices("nqmeasure8"))
    nqmeasure8_e = CKEditorField("nqmeasure8_e")
    nqmeasure9 = RadioField("nqmeasure9", choices=get_choices("nqmeasure9"))
    nqmeasure9_e = CKEditorField("nqmeasure9_e")
    nqmeasure10 = RadioField("nqmeasure10", choices=get_choices("nqmeasure10"))
    nqmeasure10_e = CKEditorField("nqmeasure10_e")
    nqmeasure11 = RadioField("nqmeasure11", choices=get_choices("nqmeasure11"))
    nqmeasure11_e = CKEditorField("nqmeasure11_e")
    nqmeasure11a = RadioField("nqmeasure11a", choices=get_choices("nqmeasure11a"))
    nqmeasure11a_e = CKEditorField("nqmeasure11a_e")
    nqmeasure11b = RadioField("nqmeasure11b", choices=get_choices("nqmeasure11b"))
    nqmeasure11b_e = CKEditorField("nqmeasure11b_e")
    nqmeasure11c = RadioField("nqmeasure11c", choices=get_choices("nqmeasure11c"))
    nqmeasure11c_e = CKEditorField("nqmeasure11c_e")
    nqmeasure11d = RadioField("nqmeasure11d", choices=get_choices("nqmeasure11d"))
    nqmeasure11d_e = CKEditorField("nqmeasure11d_e")
    nqmeasure11e = RadioField("nqmeasure11e", choices=get_choices("nqmeasure11e"))
    nqmeasure11e_e = CKEditorField("nqmeasure11e_e")
    nqmeasure12 = RadioField("nqmeasure12", choices=get_choices("nqmeasure12"))
    nqmeasure12_e = CKEditorField("nqmeasure12_e")
    nqmeasure13 = RadioField("nqmeasure13", choices=get_choices("nqmeasure13"))
    nqmeasure13_e = CKEditorField("nqmeasure13_e")
    nqmeasure14 = RadioField("nqmeasure14", choices=get_choices("nqmeasure14"))
    nqmeasure14_e = CKEditorField("nqmeasure14_e")
    nqmeasure15 = RadioField("nqmeasure15", choices=get_choices("nqmeasure15"))
    nqmeasure15_e = CKEditorField("nqmeasure15_e")
    nqmeasure16 = RadioField("nqmeasure16", choices=get_choices("nqmeasure16"))
    nqmeasure16_e = CKEditorField("nqmeasure16_e")
    nqmeasure17 = RadioField("nqmeasure17", choices=get_choices("nqmeasure17"))
    nqmeasure17_e = CKEditorField("nqmeasure17_e")
    nqmeasure18 = RadioField("nqmeasure18", choices=get_choices("nqmeasure18"))
    nqmeasure18_e = CKEditorField("nqmeasure18_e")
    methodsnq_comment = CKEditorField("methodsnq_comment")

    # Methods (questionnaire)
    qmeasure1 = RadioField("qmeasure1", choices=get_choices("qmeasure1"))
    qmeasure1_e = CKEditorField("qmeasure1_e")
    qmeasure2 = RadioField("qmeasure2", choices=get_choices("qmeasure2"))
    qmeasure2_e = CKEditorField("qmeasure2_e")
    qmeasure3 = RadioField("qmeasure3", choices=get_choices("qmeasure3"))
    qmeasure3_e = CKEditorField("qmeasure3_e")
    qmeasure4 = RadioField("qmeasure4", choices=get_choices("qmeasure4"))
    qmeasure4_e = CKEditorField("qmeasure4_e")
    qmeasure5 = RadioField("qmeasure5", choices=get_choices("qmeasure5"))
    qmeasure5_e = CKEditorField("qmeasure5_e")
    qmeasure6 = RadioField("qmeasure6", choices=get_choices("qmeasure6"))
    qmeasure6_e = CKEditorField("qmeasure6_e")
    qmeasure6a = RadioField("qmeasure6a", choices=get_choices("qmeasure6a"))
    qmeasure6a_e = CKEditorField("qmeasure6a_e")
    qmeasure6b = RadioField("qmeasure6b", choices=get_choices("qmeasure6b"))
    qmeasure6b_e = CKEditorField("qmeasure6b_e")
    qmeasure6c = RadioField("qmeasure6c", choices=get_choices("qmeasure6c"))
    qmeasure6c_e = CKEditorField("qmeasure6c_e")
    qmeasure6d = RadioField("qmeasure6d", choices=get_choices("qmeasure6d"))
    qmeasure6d_e = CKEditorField("qmeasure6d_e")
    qmeasure6e = RadioField("qmeasure6e", choices=get_choices("qmeasure6e"))
    qmeasure6e_e = CKEditorField("qmeasure6e_e")
    qmeasure6f = RadioField("qmeasure6f", choices=get_choices("qmeasure6f"))
    qmeasure6f_e = CKEditorField("qmeasure6f_e")
    qmeasure7a = RadioField("qmeasure7a", choices=get_choices("qmeasure7a"))
    qmeasure7a_e = CKEditorField("qmeasure7a_e")
    qmeasure7b = RadioField("qmeasure7b", choices=get_choices("qmeasure7b"))
    qmeasure7b_e = CKEditorField("qmeasure7b_e")
    qmeasure7c = RadioField("qmeasure7c", choices=get_choices("qmeasure7c"))
    qmeasure7c_e = CKEditorField("qmeasure7c_e")
    qmeasure7d = RadioField("qmeasure7d", choices=get_choices("qmeasure7d"))
    qmeasure7d_e = CKEditorField("qmeasure7d_e")
    qmeasure8 = RadioField("qmeasure8", choices=get_choices("qmeasure8"))
    qmeasure8_e = CKEditorField("qmeasure8_e")
    qmeasure9 = RadioField("qmeasure9", choices=get_choices("qmeasure9"))
    qmeasure9_e = CKEditorField("qmeasure9_e")
    qmeasure10 = RadioField("qmeasure10", choices=get_choices("qmeasure10"))
    qmeasure10_e = CKEditorField("qmeasure10_e")
    methodsq_comment = CKEditorField("methodsq_comment")

    # Results
    flow1 = RadioField("flow1", choices=get_choices("flow1"))
    flow1_e = CKEditorField("flow1_e")
    flow2 = RadioField("flow2", choices=get_choices("flow2"))
    flow2_e = CKEditorField("flow2_e")
    flow3 = RadioField("flow3", choices=get_choices("flow3"))
    flow3_e = CKEditorField("flow3_e")

    descriptive1 = RadioField("descriptive1", choices=get_choices("descriptive1"))

    descriptive1_e = CKEditorField("descriptive1_e")
    descriptive2 = RadioField("descriptive2", choices=get_choices("descriptive2"))
    descriptive2_e = CKEditorField("descriptive2_e")
    inferential1 = RadioField("inferential1", choices=get_choices("inferential1"))
    inferential1_e = CKEditorField("inferential1_e")
    inferential2 = RadioField("inferential2", choices=get_choices("inferential2"))
    inferential2_e = CKEditorField("inferential2_e")
    inferential3 = RadioField("inferential3", choices=get_choices("inferential3"))
    inferential3_e = CKEditorField("inferential3_e")
    results_comment = CKEditorField("results_comment")

    # Conclusions 
    interpretation = RadioField("interpretation", choices=get_choices("interpretation"))
    interpretation_e = CKEditorField("interpretation_e")
    validity = IntegerField("validity")
    validity_e = CKEditorField("validity_e")
    conclusions_comment = CKEditorField("conclusions_comment")
    save = SubmitField('Save')

class CreateArticleForm(FlaskForm):
    short = StringField('Short', validators=[DataRequired()])
    create = SubmitField('Create')


class DeleteForm(FlaskForm):
    id = IntegerField('Id')
    short = StringField('Short')
    confirm = StringField("Confirm")
    delete = SubmitField('Delete')
