import sqlite3
import datetime

def insert_booking(user_id, train_id, alphanumeric, booking_time, name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat=None):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO bookings (user_id, train_id, alphanumeric, time, date, name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, train_id, alphanumeric, booking_time.timestamp(), booking_time.strftime('%Y-%m-%d'), name, surname, address, city, credit_card, expire_date_card, number_of_tickets, seat))
    
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
    SELECT
        bookings.id, -- [0]
        bookings.user_id, -- [1]
        bookings.train_id,
        trains.alphanumeric,
        bookings.time,
        bookings.date,
        bookings.name,
        bookings.surname,
        bookings.address,
        bookings.city,
        bookings.credit_card,
        bookings.expire_date_card,
        bookings.number_of_tickets,
        bookings.seat,
        trains.departure,
        trains.arrival,
        trains.departure_date,
        trains.departure_time,
        trains.arrival_time,
        trains.train_type,
        trains.ticket_price
    FROM bookings
    LEFT JOIN trains ON bookings.train_id = trains.id
    WHERE user_id = ?
    '''
    cursor.execute(query, (user_id,))
    train = cursor.fetchall()
    conn.close()
    return train

def count_seats_for_train(train_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Query parametrizzata (per prevenire SQL injections) e passo i parametri train_id come una tupla (quindi metto una virgola dopo)
    query = '''
    SELECT SUM(number_of_tickets)
    FROM bookings
    WHERE train_id = ?
    '''
    cursor.execute(query, (train_id,))
    tickets = cursor.fetchone()
    conn.close()
    return tickets[0]

'''
    I due metodi seguenti servono per prendere dal db i bookings dato un ID, e successivamente eliminare un booking
    che corrisponda a quell'ID
'''
# def get_booking_by_id(booking_id): # With a LEFT OUTER JOIN with the TRAINS table !!!! 
    # conn = sqlite3.connect('data.db')
    # cursor = conn.cursor()

    # query = 'SELECT * FROM bookings WHERE id = ?'
    # cursor.execute(query, (booking_id,))
    # booking = cursor.fetchone()
    # conn.close()
    # return booking

def get_booking_by_id(booking_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    # Potrei migliorare questa query usando gli asterischi per selezionare ogni campo delle tabelle,
    # comunque questo è proprio l'ordine che vorrei dare alla struttura dati booking che passo di ritorno
    query = '''
    SELECT
        bookings.id,
        bookings.user_id,
        bookings.train_id,
        trains.alphanumeric,
        bookings.time,
        bookings.date,
        bookings.name,
        bookings.surname,
        bookings.address,
        bookings.city,
        bookings.credit_card,
        bookings.expire_date_card,
        bookings.number_of_tickets,
        bookings.seat,
        trains.departure,
        trains.arrival,
        trains.departure_date,
        trains.departure_time,
        trains.arrival_time,
        trains.train_type,
        trains.ticket_price
    FROM bookings
    LEFT JOIN trains ON bookings.train_id = trains.id
    WHERE bookings.id = ?
    '''
    cursor.execute(query, (booking_id,))
    booking = cursor.fetchone()
    conn.close()
    return booking

def delete_booking(booking_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    query = 'DELETE FROM bookings WHERE id = ?'
    cursor.execute(query, (booking_id,))
    conn.commit()
    conn.close()

#def modify_booking(booking_id):
    #conn = sqlite3.connect('data.db')
    #cursor = conn.cursor()

    #query = 'DELETE FROM bookings WHERE id = ?'
    #cursor.execute(query, (booking_id,))
    #conn.commit()
    #conn.close()
