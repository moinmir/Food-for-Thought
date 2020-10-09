from flask import render_template, request, Blueprint
from food.models import Post


main = Blueprint('main', __name__)

@main.route("/")  # home page
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5, page=page)
    return render_template("home.html", posts=posts, title="Home")


@main.route("/about")  # home page
def about():
    return render_template("about.html", title="About")
