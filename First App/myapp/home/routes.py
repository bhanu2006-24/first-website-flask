# myapp/home/routes.py
from flask import Blueprint, render_template, session, redirect, url_for
from myapp.models import User , BlogPost
from flask_login import current_user

home = Blueprint('home', __name__ , template_folder='templates/home')

@home.route('/')
def index():
    public_blogs = BlogPost.query.filter_by(is_public=True).all()
    return render_template('home.html', public_blogs=public_blogs)
@home.route('/members')
def members(): 
    users = User.query.all()
    return render_template('members.html', members=[u.username for u in users])

@home.route('/test-login')
def test_login():
    if current_user.is_authenticated:
        return f"Logged in as {current_user.username}"
    else:
        return "Not logged in"
