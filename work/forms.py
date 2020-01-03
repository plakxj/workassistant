#-*-coding:GBK -*- 

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length
import sys


class RecordForm(FlaskForm):
    subject = StringField("主题",validators=[DataRequired()])
    keyword1 = StringField("关键字",validators=[DataRequired()])
    keyword2 = StringField("时间", validators=[DataRequired()])
    text = StringField("内容", validators=[DataRequired()])
    submit = SubmitField("保存")

class ShowForm(FlaskForm):
    subject = StringField("主题",validators=[DataRequired()])
    keyword1 = StringField("关键字",validators=[DataRequired()])
    keyword2 = StringField("时间",validators=[DataRequired()])
    text = StringField("内容",validators=[DataRequired()])
    save = SubmitField("保存")

class EditForm(FlaskForm):
    subject = StringField("主题",validators=[DataRequired()])
    keyword1 = StringField("关键字",validators=[DataRequired()])
    keyword2 = StringField("时间",validators=[DataRequired()])
    text = StringField("内容", validators=[DataRequired()])
    update = SubmitField("更新")

class DeleteForm(FlaskForm):
    delete = SubmitField("删除")
