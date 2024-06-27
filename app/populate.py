import sqlite3

def populate():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    trains_data = [
    ("TR001", "2024-06-29", "Torino", "Milano", 800, 1000, "Weekdays", "Regular", 20),
    ("TR002", "2024-07-04", "Torino", "Milano", 820, 1020, "Holidays", "Regular", 30),
    ("TR003", "2024-07-04", "Torino", "Milano", 920, 1120, "Holidays", "Regular", 30),
    ("TR004", "2024-07-04", "Torino", "Milano", 1020, 1220, "Holidays", "Regular", 30),
    ("TR005", "2024-07-10", "Torino", "Milano", 840, 1040, "Everyday", "Regular", 20),
    ("TR006", "2024-07-01", "Torino", "Milano", 900, 1100, "Weekdays", "High-speed", 30),
    ("TR007", "2024-07-07", "Torino", "Milano", 920, 1120, "Everyday", "High-speed", 30),

    ("TR008", "2024-06-30", "Milano", "Roma", 930, 1300, "Weekdays", "Regular", 120),
    ("TR008", "2024-06-30", "Milano", "Roma", 1030, 1400, "Weekdays", "Regular", 120),
    ("TR008", "2024-06-30", "Milano", "Roma", 1130, 1500, "Weekdays", "Regular", 120),
    ("TR009", "2024-07-02", "Milano", "Roma", 950, 1320, "Holydays", "High-speed", 180),
    ("TR009", "2024-07-02", "Milano", "Roma", 1050, 1420, "Holydays", "High-speed", 180),
    ("TR009", "2024-07-02", "Milano", "Roma", 1150, 1520, "Holydays", "High-speed", 180),
    ("TR010", "2024-06-28", "Milano", "Roma", 1000, 1400, "Everyday", "High-speed", 180),
    ("TR011", "2024-07-09", "Milano", "Roma", 1020, 1420, "Weekdays", "Regular", 120),
    ("TR012", "2024-07-11", "Milano", "Roma", 1040, 1440, "Holydays", "High-speed", 180),

    ("TR013", "2024-07-05", "Roma", "Torino", 700, 1100, "Weekdays", "High-speed", 60),
    ("TR014", "2024-07-06", "Roma", "Torino", 720, 1120, "Holidays", "Regular", 40),
    ("TR015", "2024-07-03", "Roma", "Torino", 740, 1140, "Everyday", "High-speed", 60),
    ("TR015", "2024-07-03", "Roma", "Torino", 840, 1240, "Everyday", "High-speed", 60),
    ("TR015", "2024-07-03", "Roma", "Torino", 940, 1340, "Everyday", "High-speed", 60),
    ("TR016", "2024-07-08", "Roma", "Torino", 800, 1200, "Weekdays", "Regular", 40),
    ("TR017", "2024-07-11", "Roma", "Torino", 820, 1220, "Everyday", "High-speed", 60)
    ]

    insert_query = '''
    INSERT INTO trains (alphanumeric, departure_date, departure, arrival, departure_time, arrival_time, days_of_operation, train_type, ticket_price)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
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

def populate_train_capacity():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    train_capacity_data = [
        ("Regular", 20),
        ("High-speed", 30)
    ]

    insert_query = '''
    INSERT INTO train_capacity (train_type, capacity)
    VALUES (?, ?)
    '''

    try:
        cursor.executemany(insert_query, train_capacity_data)
        conn.commit()
        print("Data inserted successfully into the train_capacity table.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    finally:
        conn.close()


# def populate_solutions():

    # conn = sqlite3.connect('data.db')
    # cursor = conn.cursor()

    # solutions_data = [
    # ]

    # insert_query = '''
    # INSERT INTO ()
    # VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    # '''

    # # Safer
    # try:
        # cursor.executemany(insert_query, solutions_data)
        # conn.commit()
        # print("Data inserted successfully into the trains table.")
    # except sqlite3.IntegrityError as e:
        # print(f"IntegrityError: {e}")
    # finally:
        # conn.close()

    # # # Less safe
    # # cursor.executemany(insert_query, trains_data)
    # # conn.commit()
    # # conn.close()

    # print("Data inserted successfully into the solutions table.")
