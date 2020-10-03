from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "7501d06b12422d9792968f951c600b32"

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


@app.route("/about")  # home page
def about():
    return render_template("about.html", title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)