from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "7501d06b12422d9792968f951c600b32"
app.config["GOOGLEMAPS_KEY"] = "AIzaSyAOhs8UoLOWiqJwDXie6Igf8TJWw-IQkQM"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# Initialize the extensions
maps = GoogleMaps(app)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

bcrypt = Bcrypt(app)

from food import routes