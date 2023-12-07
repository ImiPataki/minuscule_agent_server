from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = False
app.testing = False
app.config.from_object(Config)
db = SQLAlchemy(app)


# The bottom import is a workaround to circular imports, a common problem with Flask applications.
from app import routes, models, errors


