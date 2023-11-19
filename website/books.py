from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required, check_auth
from website.db import get_db

bp = Blueprint('books', __name__, url_prefix='/books')

# Books--------------------------------------------------------------------------------------------------
@bp.route('/books', methods=('GET', 'POST'))
@login_required
def books():
    return render_template('books/books.html')

@bp.route('/book_inventory', methods=('GET', 'POST'))
@login_required
def book_inventory():
    db = get_db()
    books = db.execute(
        "SELECT * FROM books" 
    ).fetchall()
    return render_template('books/book_inventory.html', books=books)

@bp.route('/<isbn>/book_info', methods=('GET', 'POST'))
@login_required
def book_info(isbn):
    db = get_db()
    book = db.execute(
        'SELECT * FROM books WHERE isbn = ?', (isbn,)
    ).fetchone()
    return render_template('books/book_info.html', book=book)

@bp.route('/my_books', methods=('GET', 'POST'))
@login_required
def my_books():
    # Only Students have access because only students can borrow books
    if check_auth('student') == False:
        return redirect(url_for('index'))
    
    db = get_db()
    my_books = db.execute(
        'SELECT bor.isbn, bor.username, b.title, b.author '
        'FROM borrowed_by bor JOIN books b ON bor.isbn = b.isbn '
        'WHERE bor.username = ?', (g.user['username'],)
    ).fetchall()
    return render_template('books/my_books.html', my_books=my_books)

@bp.route('/<isbn>/borrow', methods=('POST',))
@login_required
def borrow(isbn):
    db = get_db()
    quantity = db.execute(
        'SELECT quantity FROM books WHERE isbn = ?', (isbn,)
    ).fetchone()
    book_check = db.execute(
        'SELECT COUNT(*) FROM borrowed_by WHERE isbn = ? AND username = ?',
        (isbn, g.user['username'])
    ).fetchone()
    # Checks if book is already borrowed by student
    if book_check[0] == 0:
        if quantity['quantity'] > 0:
            db.execute(
                'INSERT INTO borrowed_by (isbn, username) ' 
                'VALUES (?, ?)', (isbn, g.user['username'])
            )
            db.execute(
                'UPDATE books SET quantity = quantity - 1 '
                'WHERE isbn = ?', (isbn,)
            )
            db.commit()
        else:
            flash('Book is not available.')
    else:
        flash('You are already borrowing this book.')
    return redirect(url_for('books.my_books'))

@bp.route('/<isbn>/return_book', methods=('POST',))
@login_required
def return_book(isbn):
    db = get_db()
    db.execute(
        'DELETE FROM borrowed_by WHERE isbn = ? AND username = ?',
        (isbn, g.user['username'])
    )
    db.execute(
        'UPDATE books SET quantity = quantity + 1 '
        'WHERE isbn = ?', (isbn,)
    )
    db.commit()
    flash('Book successfully returned.')

    return redirect(url_for('books.my_books'))


@bp.route('books/manage_books', methods=('GET', 'POST'))
@login_required
def manage_books():
    # Only librarians and admins can access this page
    if check_auth('student') == True: 
        return redirect(url_for('index'))
    return render_template('books/manage_books.html')