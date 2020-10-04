from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_googlemaps import GoogleMaps, Map
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "7501d06b12422d9792968f951c600b32"
app.config["GOOGLEMAPS_KEY"] = "AIzaSyAOhs8UoLOWiqJwDXie6Igf8TJWw-IQkQM"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# Initialize the extensions
maps = GoogleMaps(app)
db = SQLAlchemy(app)


# class models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# THIS HAS TO BE ATTACHED TO DATABASE
locations = [
    {
        "icon": "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
        "lat": 37.4419,
        "lng": -122.1419,
        "infobox": "<b>Hello World</b>",
    },
    {
        "icon": "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
        "lat": 37.4300,
        "lng": -122.1400,
        "infobox": "<b>Hello World from other place</b>",
    },
]


@app.route("/")  # home page
@app.route("/home")
def home():
    return render_template("home.html", title="Home")


@app.route("/map")
def mapview():
    # creating a map in the view
    sndmap = Map(identifier="sndmap", lat=37.4419, lng=-122.1419, markers=locations)
    return render_template("map.html", sndmap=sndmap)


@app.route("/about")  # home page
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(message=f"Account created for {form.username.data}!", category="success")
        return redirect(url_for("home"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if (
            form.email.data == "faisal@foodforthought.com"
            and form.password.data == "faisalsucksass"
        ):
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.", "danger")

    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)