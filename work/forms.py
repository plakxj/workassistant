from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length

class RecordForm(FlaskForm):
    subject = StringField("subject",validators=[DataRequired()])
    keyword1 = StringField("keyword1",validators=[DataRequired()])
    keyword2 = StringField("keyword2", validators=[DataRequired()])
    text = StringField("text", validators=[DataRequired()])
    submit = SubmitField("save")

class ShowForm(FlaskForm):
    subject = StringField("subject",validators=[DataRequired()])
    keyword1 = StringField("keyword1",validators=[DataRequired()])
    keyword2 = StringField("keyword2", validators=[DataRequired()])
    text = StringField("text", validators=[DataRequired()])
    save = SubmitField("save")

class EditForm(FlaskForm):
    subject = StringField("subject",validators=[DataRequired()])
    keyword1 = StringField("keyword1",validators=[DataRequired()])
    keyword2 = StringField("keyword2", validators=[DataRequired()])
    text = StringField("text", validators=[DataRequired()])
    update = SubmitField("update")

class DeleteForm(FlaskForm):
    delete = SubmitField("delete")
