from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.models import Participants
from flask import Blueprint
from app.main import main_bp

main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/about')
def about():
    return render_template('main/about.html')


@main_bp.route('/profile')
@login_required
def profile():
    return render_template('main/profile.html', name=current_user.first_name)

@main_bp.route('/database')
@login_required
def database():
    return render_template('main/database.html', participants=Participants)
