from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAOhs8UoLOWiqJwDXie6Igf8TJWw-IQkQM"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SECRET_KEY'] = "7501d06b12422d9792968f951c600b32"

# app config for email
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "officialfoodforthought@gmail.com"
app.config['MAIL_PASSWORD'] = "food.for.thought"

# Initialize the extensions
db = SQLAlchemy(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = "users.login"
login_manager.login_message_category = "info"


from food.users.routes import users
from food.campaigns.routes import campaigns
from food.main.routes import main
from food.transactions.routes import transactions
app.register_blueprint(users)
app.register_blueprint(campaigns)
app.register_blueprint(main)
app.register_blueprint(transactions)


