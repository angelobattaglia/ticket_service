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
