from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user
from food import db
from food.models import Campaign
from food.campaigns.forms import CampaignForm
from food.campaigns.utils import login_required, save_picture

campaigns = Blueprint("campaigns", __name__)


@campaigns.route("/campaign/new", methods=["GET", "POST"])
@login_required(role="Restaurant")
def new_campaign():
    form = CampaignForm()
    if form.validate_on_submit():
        campaign = Campaign(
            title=form.title.data,
            content=form.content.data,
            goal=form.goal.data,
            owner=current_user,
        )
        db.session.add(campaign)
        db.session.commit()

        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data)

        db.session.commit()
        flash("Your campaign has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template(
        "create_campaign.html", title="New Campaign", form=form, legend="New Campaign"
    )


@campaigns.route("/campaign/<int:campaign_id>")
def campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    return render_template("campaign.html", title=campaign.title, campaign=campaign)


@campaigns.route("/campaign/<int:campaign_id>/update", methods=["GET", "POST"])
@login_required(role="Restaurant")
def update_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)

    if campaign.owner != current_user:
        abort(403)

    form = CampaignForm()
    if form.validate():
        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data)

        campaign.title = form.title.data
        campaign.content = form.content.data
        campaign.goal = form.goal.data
        db.session.commit()
        flash("Your campaign has been updated!", "success")
        return redirect(url_for("campaigns.campaign", campaign_id=campaign.id))
    elif request.method == "GET":
        form.title.data = campaign.title
        form.content.data = campaign.content
        form.goal.data = campaign.goal
    return render_template(
        "create_campaign.html",
        title="Update Campaign",
        form=form,
        legend="Update Campaign",
    )


@campaigns.route("/campaign/<int:campaign_id>/delete", methods=["POST"])
@login_required(role="Restaurant")
def delete_campaign(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    if campaign.owner != current_user:
        abort(403)
    db.session.delete(campaign)
    db.session.commit()
    flash("Your campaign has been deleted!", "success")
    return redirect(url_for("main.home"))
