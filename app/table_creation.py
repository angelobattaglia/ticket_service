import sqlite3

def create_table_users():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "users" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "email" TEXT NOT NULL UNIQUE,
            "password" TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def create_table_trains():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "trains" (
	        "id"	INTEGER NOT NULL UNIQUE,
	        "alphanumeric"	TEXT NOT NULL UNIQUE,
            "departure_date" TEXT NOT NULL,
	        "departure"	TEXT NOT NULL,
	        "arrival"	TEXT NOT NULL,
	        "departure_time"	INTEGER NOT NULL,
	        "arrival_time"	INTEGER NOT NULL,
	        "days_of_operation"	TEXT NOT NULL,
	        "train_type"	TEXT NOT NULL,
	        "ticket_price"	INTEGER NOT NULL,
	        PRIMARY KEY("id" AUTOINCREMENT)
        );
    ''')
    conn.commit()
    conn.close

def create_table_bookings():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "bookings" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL,
            "train_id" INTEGER NOT NULL,
            "alphanumeric" TEXT NOT NULL,

            -- "time" mi serve per permettere la cancellazione o la modifica di un biglietto, acquistato in precedenza, fino a 2 minuti prima della partenza
            "time" INTEGER NOT NULL,
            -- "date": TODO
            "date" TEXT NOT NULL,

            -- Informazioni sull'acquirente
            "name" TEXT NOT NULL,
            "surname" TEXT NOT NULL,
            "address" TEXT NOT NULL,
            "city" TEXT NOT NULL,
            "credit_card" TEXT NOT NULL,
            "expire_date_card" TEXT NOT NULL,

            -- Informazioni su quanti biglietti si vogliano acquistare
            "number_of_tickets" INTEGER NOT NULL,
            "seat" INTEGER, -- va da 0 a 30, implementare con un menu drop-down, facoltativo, operativo nel caso in cui sia un treno ad alta velocita'

            FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
            FOREIGN KEY ("train_id") REFERENCES "trains" ("id"), -- open question: would it be better to use "alphanumeric" from trains instead? 
            FOREIGN KEY ("alphanumeric") REFERENCES "trains" ("alphanumeric")
        );
    ''')
    conn.commit()
    conn.close

# def create_table_solutions():
    # conn = sqlite3.connect('data.db')
    # cursor = conn.cursor()
    # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS "solutions" (
            # "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            # "train_alphanumeric" TEXT NOT NULL,
	        # "arrival"	NUMERIC NOT NULL,
	        # "departure_time"	INTEGER NOT NULL,
            # "train_type"    TEXT NOT NULL,
            # "current_capacity"      INTEGER NOT NULL, 
            # "max_capacity"      INTEGER NOT NULL,
            # "ticket_price"      INTEGER NOT NULL,

            # FOREIGN KEY ("train_alphanumeric") REFERENCES "trains" ("alphanumeric")
        # );
    # ''')
    # conn.commit()
    # conn.close

