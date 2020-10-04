from flask import render_template, url_for, flash, redirect
from food import app, db, bcrypt
from food.forms import RegistrationForm, LoginForm
from food.models import User, Post
from flask_googlemaps import Map
from flask_login import login_user


# Dummy Data
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
posts = [
    {
        "restaurant": "Olives",
        "title": "Pizzas for nurses in County Hospital",
        "content": "Help us raise money to send 100 pizzas to nurses in the County Hospital.",
        "goal": 40,
        "date_posted": "October 3, 2020",
    },
    {
        "restaurant": "Tacoria",
        "title": "Tacos for kids in orphanage",
        "content": "Help us raise money to send 500 tacos to 6 orphanages in the district.",
        "goal": 100,
        "date_posted": "October 5, 2020",
    },
]


@app.route("/")  # home page
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")


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
        # created user and adding to database
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = User(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        flash(
            message="Your account has been created! You can now log in",
            category="success",
        )
        return redirect(url_for("login"))

    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password.", "danger")

    return render_template("login.html", title="Login", form=form)