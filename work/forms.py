#-*-coding:GBK -*- 

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
import sys


class RecordForm(FlaskForm):
    subject = StringField("����",validators=[DataRequired()])
    keyword1 = StringField("�ؼ���",validators=[DataRequired()])
    keyword2 = StringField("ʱ��", validators=[DataRequired()])
    text = StringField("����", validators=[DataRequired()])
    submit = SubmitField("����")

class ShowForm(FlaskForm):
    subject = StringField("����",validators=[DataRequired()])
    keyword1 = StringField("�ؼ���",validators=[DataRequired()])
    keyword2 = StringField("ʱ��",validators=[DataRequired()])
    text = StringField("����",validators=[DataRequired()])
    save = SubmitField("����")

class EditForm(FlaskForm):
    subject = StringField("����",validators=[DataRequired()])
    keyword1 = StringField("�ؼ���",validators=[DataRequired()])
    keyword2 = StringField("ʱ��",validators=[DataRequired()])
    text = StringField("����", validators=[DataRequired()])
    update = SubmitField("����")

class DeleteForm(FlaskForm):
    delete = SubmitField("ɾ��")
