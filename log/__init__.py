from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../users.db'
app.app_context().push()
db = SQLAlchemy(app)

from log import routes