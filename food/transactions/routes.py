from flask import Blueprint, render_template, url_for, flash, redirect
from food.transactions.forms import DonateForm
from flask_login import current_user
from food.models import Campaign, Transaction
from food import db
from food.transactions.utils import login_required

transactions = Blueprint('transactions', __name__)

@transactions.route("/campaign/<int:campaign_id>/donate", methods=["GET", "POST"])
@login_required(role="Donor")
def donate(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    form = DonateForm()

    if form.validate_on_submit():
        order = Transaction(amount=form.amount.data, donor=current_user, campaign=campaign)
        db.session.add(order)
        db.session.commit()
        flash("Your donation has been sent!", "success")
        return redirect(url_for('main.home'))

    return render_template("make_donation.html", title="Donate", form=form)