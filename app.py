from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_googlemaps import GoogleMaps, Map

app = Flask(__name__)

app.config["SECRET_KEY"] = "7501d06b12422d9792968f951c600b32"

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAOhs8UoLOWiqJwDXie6Igf8TJWw-IQkQM"

# Initialize the extension
GoogleMaps(app)

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

#THIS HAS TO BE ATTACHED TO DATABASE
locations = [
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]

@app.route("/")  # home page
@app.route("/home")
def home():
    return render_template("home.html", posts=posts, title="Home")

@app.route("/map")
def mapview():
    # creating a map in the view
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers= locations
    )
    return render_template('map.html', sndmap=sndmap)

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