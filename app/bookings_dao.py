import sqlite3
import datetime

def insert_booking(user_id, train_id, booking_time, name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat=None):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO bookings (user_id, train_id, time, date, name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, train_id, booking_time.timestamp(), booking_time.strftime('%Y-%m-%d'), name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat))
    conn.commit()
    conn.close()

'''
    The following method "get_bookings_for_user()" receives "user_id" as an input and retrieves all the bookings in the "bookings" table (from data.db)
    that have been made by the user with "user_id" as a identifier
'''
def get_bookings_for_user(user_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Query parametrizzata (per prevenire SQL injections) e passo i parametri train_id come una tupla (quindi metto una virgola dopo)
    query = '''
    SELECT * FROM bookings
    WHERE user_id = ?
    '''
    cursor.execute(query, (user_id,))
    train = cursor.fetchall()
    conn.close()
    return train
