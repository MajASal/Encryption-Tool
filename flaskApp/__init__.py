from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'OPAW)SUE&&ashdljkashdjkasbfaosfjasof'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
User = Base.classes.user
session = Session

from flaskApp import webapp