from flask import Blueprint, render_template, url_for, flash, redirect
from food.transactions.forms import OrderForm
from flask_login import login_required, current_user
from food.models import Post
from food import db

transactions = Blueprint('transactions', __name__)

@transactions.route("/post/<int:post_id>/donate", methods=["GET", "POST"])
@login_required
def donate(post_id):
    post = Post.query.get_or_404(post_id)
    form = OrderForm()

    if form.validate_on_submit():
        post.author.orders = int(post.author.orders) + int(form.amount.data)
        db.session.commit()
        flash("Your donation has been sent!", "success")
        return redirect(url_for('main.home'))

    return render_template("make_donation.html", title="Donate", form=form)