import sqlite3
import datetime

# Function to add a new train capacity
def add_train_capacity(train_type, capacity):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO train_capacity (train_type, capacity)
        VALUES (?, ?)
    ''', (train_type, capacity))
    conn.commit()
    conn.close()

# Function to retrieve the capacity for a specific train type
def get_train_capacity(train_type):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT capacity FROM train_capacity
        WHERE train_type = ?
    ''', (train_type,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Function to update the capacity for a specific train type
def update_train_capacity(train_type, new_capacity):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE train_capacity
        SET capacity = ?
        WHERE train_type = ?
    ''', (new_capacity, train_type))
    conn.commit()
    conn.close()

# Function to delete a train capacity record
def delete_train_capacity(train_type):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM train_capacity
        WHERE train_type = ?
    ''', (train_type,))
    conn.commit()
    conn.close()

# Function to list all train capacities
def list_train_capacities():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM train_capacity
    ''')
    results = cursor.fetchall()
    conn.close()
    return results

