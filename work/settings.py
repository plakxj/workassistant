# -*- coding: utf-8 -*-

import os


dev_db = "sqlite:///" + os.path.join("WORKON_HOME","data.db")


SECRET_KEY = os.getenv("SECRET_KEY","secret string")


SQLAHCHEMY_TRACK_MODIFICATIONS = True


SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI",dev_db)
