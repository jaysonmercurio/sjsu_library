from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required, check_auth
from website.db import get_db

bp = Blueprint('user', __name__)

@bp.route('/')
@login_required
def user():
    return render_template('user/index.html')

@bp.route('/books', methods=('GET', 'POST'))
@login_required
def books():
    db = get_db()
    books = db.execute(
        "SELECT isbn, author, quantity "
        "FROM books" 
    ).fetchall()
    return render_template('user/books.html', books=books)

@bp.route('/rooms', methods=('GET', 'POST'))
@login_required
def rooms():
    return render_template('user/rooms.html')

# Managing Users------------------------------------------
@bp.route('/manage_users', methods=('GET', 'POST'))
@login_required
def manage_users():
    if check_auth('admin') == False:
        return redirect(url_for('index'))
    
    db = get_db()
    users = db.execute(
        "SELECT u.username, u.first_name, u.last_name, r.role_name, r.approval "
        "FROM users u JOIN roles r ON u.username = r.username " 
        "WHERE u.username != ? ORDER BY r.role_name, u.last_name", (g.user['username'],)
    ).fetchall()
    return render_template('user/manage_users.html', users=users)

@bp.route('/<username>/update_user', methods=('GET', 'POST'))
@login_required
def update_user(username):
    if check_auth('admin') == False:
        return redirect(url_for('index'))
    db = get_db()
    user = db.execute(
        "SELECT u.username, u.first_name, u.last_name, r.role_name, r.approval "
        "FROM users u JOIN roles r ON u.username = r.username " 
        "WHERE u.username = ?", (username,)
    ).fetchone()
    return render_template('user/update_user.html', user=user)

@bp.route('/<username>/approve_user', methods=('GET', 'POST'))
@login_required
def approve_user(username):
    if check_auth('admin') == False:
        return redirect(url_for('index'))
    
    db = get_db()
    db.execute('UPDATE roles SET approval = 1 WHERE username = ?', (username,))
    db.commit()
    flash('User successfully approved.')
    return redirect(url_for('user.manage_users'))

@bp.route('/<username>/delete_user', methods=('POST',))
@login_required
def delete_user(username):
    if check_auth('admin') == False:
        return redirect(url_for('index'))

    db = get_db()
    db.execute('DELETE FROM users WHERE username = ?', (username,))
    db.execute('DELETE FROM roles WHERE username = ?', (username,))
    db.commit()
    flash('User successfully deleted.')
    return redirect(url_for('user.manage_users'))