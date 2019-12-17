
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("work")
app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blockss = True

db = SQLAlchemy(app)

from work import views,errors,commands


