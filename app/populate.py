import sqlite3

def populate():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    trains_data = [
        ("TR001", "Torino", "Milano", 800, 1000, "Mon,Tue,Wed,Thu,Fri", "Regular", 20),
        ("TR002", "Torino", "Milano", 820, 1020, "Sat,Sun", "Regular", 30),
        ("TR003", "Torino", "Milano", 840, 1040, "Mon,Wed,Fri", "Regular", 20),
        ("TR004", "Torino", "Milano", 900, 1100, "Tue,Thu,Sat", "High-speed", 30),
        ("TR005", "Torino", "Milano", 920, 1120, "Everyday", "High-speed", 30),

        ("TR006", "Milano", "Roma", 930, 1300, "Mon,Wed,Fri,Sun", "Regular", 120),
        ("TR007", "Milano", "Roma", 950, 1320, "Tue,Thu,Sat", "High-speed", 180),
        ("TR008", "Milano", "Roma", 1000, 1400, "Mon,Wed,Fri,Sun", "High-speed", 180),
        ("TR009", "Milano", "Roma", 1020, 1420, "Everyday", "Regular", 120),
        ("TR010", "Milano", "Roma", 1040, 1440, "Mon,Tue,Thu,Sat", "High-speed", 180),

        ("TR011", "Roma", "Torino", 700, 1100, "Everyday", "High-speed", 60),
        ("TR012", "Roma", "Torino", 720, 1120, "Mon,Wed,Fri", "Regular", 40),
        ("TR013", "Roma", "Torino", 740, 1140, "Tue,Thu,Sat", "High-speed", 60),
        ("TR014", "Roma", "Torino", 800, 1200, "Everyday", "Regular", 40),
        ("TR015", "Roma", "Torino", 820, 1220, "Mon,Wed,Fri,Sun", "High-speed", 60)
    ]

    insert_query = '''
    INSERT INTO trains (alphanumeric, departure, arrival, departure_time, arrival_time, days_of_operation, train_type, ticket_price)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Safer
    try:
        cursor.executemany(insert_query, trains_data)
        conn.commit()
        print("Data inserted successfully into the trains table.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    finally:
        conn.close()

    # # Less safe
    # cursor.executemany(insert_query, trains_data)
    # conn.commit()
    # conn.close()

    print("Data inserted successfully into the trains table.")


def populate_solutions():

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    solutions_data = [
    ]

    insert_query = '''
    INSERT INTO ()
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''

    # Safer
    try:
        cursor.executemany(insert_query, solutions_data)
        conn.commit()
        print("Data inserted successfully into the trains table.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    finally:
        conn.close()

    # # Less safe
    # cursor.executemany(insert_query, trains_data)
    # conn.commit()
    # conn.close()

    print("Data inserted successfully into the solutions table.")
