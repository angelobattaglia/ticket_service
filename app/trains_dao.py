import sqlite3
import datetime

def search_trains(departure_city, arrival_city, departure_date):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    # Convert the departure_date to a day of the week (e.g., 'Monday')
    day_of_week = datetime.datetime.strptime(departure_date, '%Y-%m-%d').strftime('%A')
    
    query = '''
        SELECT trains.*,train_capacity.capacity, train_capacity.capacity - ifnull((select SUM(number_of_tickets) FROM bookings WHERE train_id = trains.id),0) as booked FROM trains
        LEFT JOIN train_capacity ON trains.train_type = train_capacity.train_type
        WHERE departure = ?
        AND arrival = ?
        AND departure_date = ?
    '''

    cursor.execute(query, (departure_city, arrival_city, departure_date))

    results = cursor.fetchall()
    conn.close()
    return results

def get_train_by_id(train_id): 
    conn = sqlite3.connect('data.db') 
    cursor = conn.cursor() 
 
    # Query parametrizzata (per prevenire SQL injections) e passo i parametri train_id come una tupla (quindi metto una virgola dopo) 
    query = ''' 
    SELECT * FROM trains 
    WHERE id = ? 
    ''' 
    cursor.execute(query, (train_id,)) 
    train = cursor.fetchone() 
    conn.close() 
    return train

def get_train_by_alphanumeric(alphanumeric): 
    conn = sqlite3.connect('data.db') 
    cursor = conn.cursor() 
 
    # Query parametrizzata (per prevenire SQL injections) e passo i parametri train_id come una tupla (quindi metto una virgola dopo) 
    query = ''' 
    SELECT * FROM trains 
    WHERE alphanumeric = ? 
    ''' 
    cursor.execute(query, (alphanumeric,)) 
    train = cursor.fetchone() 
    conn.close() 
    return train

def get_trains():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM trains')
    trains = cursor.fetchall()
    conn.close()
    return trains
