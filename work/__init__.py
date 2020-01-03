# -*- coding: utf-8 -*-  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("work")
app.config.from_pyfile("settings.py")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blockss = True

db = SQLAlchemy(app)

from work import views,forms,settings,models








