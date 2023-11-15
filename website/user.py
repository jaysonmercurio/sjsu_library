from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db

bp = Blueprint('user', __name__)

@bp.route('/')
@login_required
def user():
    return render_template('index.html')