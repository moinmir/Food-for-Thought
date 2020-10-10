from flask import render_template, request, Blueprint
from food.models import Campaign


main = Blueprint('main', __name__)

@main.route("/")  # home page
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    campaigns = Campaign.query.order_by(Campaign.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", campaigns=campaigns, title="Home")


@main.route("/about") 
def about():
    return render_template("about.html", title="About")
