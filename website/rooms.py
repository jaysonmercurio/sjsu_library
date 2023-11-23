# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for
# )
# from werkzeug.exceptions import abort

# from website.auth import login_required, check_auth
# from website.db import get_db

# bp = Blueprint('rooms', __name__, url_prefix='/rooms')

# # Rooms--------------------------------------------------------------------------------------------------
# @bp.route('/rooms', methods=('GET', 'POST'))
# @login_required
# def rooms():
#     db = get_db()
#     rooms = db.execute(
#         "SELECT * FROM rooms"
#     ).fetchall()
#     return render_template('rooms/rooms.html', rooms=rooms)

# @bp.route('/<room_num>/room_info', methods=('GET', 'POST'))
# @login_required
# def room_info(room_num):
#     db = get_db()
#     room = db.execute(
#         'SELECT * FROM rooms WHERE room_num = ?', (room_num,)
#     ).fetchone()
#     booked_times = db.execute(
#         'SELECT * FROM reserve_room WHERE room_num ?', (room_num)
#     ).fetchall()
#     return render_template('books/book_info.html', room=room,booked_times=booked_times)

# @bp.route('/my_reservations', methods=('GET', 'POST'))
# @login_required
# def my_books():
#     # Everyone has access to reserving rooms
    
#     db = get_db()
#     my_reservations = db.execute(
#         'SELECT * FROM reserve_room WHERE username = ?', (g.user['username'],)
#     ).fetchall()
#     return render_template('books/my_books.html', my_reservations=my_reservations)

# @bp.route('/<room_num>/<datetime>/reserve', methods=('POST',))
# @login_required
# def borrow(room_num, datetime):
#     db = get_db()
#     check_reservation = db.execute(
#         'SELECT * FROM reserve_room '
#         'WHERE room_num = ? AND datetime = ?', (room_num, datetime,)
#     ).fetchone()
#     if check_reservation:
        
#     book_check = db.execute(
#         'SELECT COUNT(*) FROM borrowed_by WHERE isbn = ? AND username = ?',
#         (isbn, g.user['username'])
#     ).fetchone()
#     # Checks if book is already borrowed by student
#     if book_check[0] == 0:
#         if quantity['quantity'] > 0:
#             db.execute(
#                 'INSERT INTO borrowed_by (isbn, username) ' 
#                 'VALUES (?, ?)', (isbn, g.user['username'])
#             )
#             db.execute(
#                 'UPDATE books SET quantity = quantity - 1 '
#                 'WHERE isbn = ?', (isbn,)
#             )
#             db.commit()
#         else:
#             flash('Book is not available.')
#     else:
#         flash('You are already borrowing this book.')
#     return redirect(url_for('books.my_books'))

# @bp.route('/<isbn>/return_book', methods=('POST',))
# @login_required
# def return_book(isbn):
#     db = get_db()
#     db.execute(
#         'DELETE FROM borrowed_by WHERE isbn = ? AND username = ?',
#         (isbn, g.user['username'])
#     )
#     db.execute(
#         'UPDATE books SET quantity = quantity + 1 '
#         'WHERE isbn = ?', (isbn,)
#     )
#     db.commit()
#     flash('Book successfully returned.')

#     return redirect(url_for('books.my_books'))


# @bp.route('books/manage_books', methods=('GET', 'POST'))
# @login_required
# def manage_books():
#     # Only librarians and admins can access this page
#     if check_auth('student') == True: 
#         return redirect(url_for('index'))
#     return render_template('books/manage_books.html')