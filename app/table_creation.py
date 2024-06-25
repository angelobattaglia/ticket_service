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
	        "departure"	TEXT NOT NULL,
	        "arrival"	NUMERIC NOT NULL,
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

def create_table_solutions():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "solutions" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "train_alphanumeric" TEXT NOT NULL,
	        "arrival"	NUMERIC NOT NULL,
	        "departure_time"	INTEGER NOT NULL,
            "train_type"    TEXT NOT NULL,
            "capacity"      INTEGER NOT NULL, 
            "max_capacity"      INTEGER NOT NULL,
            "ticket_price"      INTEGER NOT NULL,

            FOREIGN KEY ("train_alphanumeric") REFERENCES "trains" ("alphanumeric")
        );
    ''')
    conn.commit()
    conn.close

def create_table_tickets():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "tickets" (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL,
            "solution" INTEGER NOT NULL,

            "name" TEXT NOT NULL,
            "surname" TEXT NOT NULL,
            "address" TEXT NOT NULL,
            "city" TEXT NOT NULL,
            "credit_card" TEXT NOT NULL,
            "expire_date_card" TEXT NOT NULL,

            "number_of_tickets" INTEGER NOT NULL,
            "seat" INTEGER, -- va da 1 a 30, implementare con un menu drop-down, facoltativo, operativo nel caso in cui sia un treno ad alta velocita'

            FOREIGN KEY ("user_id") REFERENCES "users" ("id"),
            FOREIGN KEY ("solution") REFERENCES "solutions" ("id")
        );
    ''')
    conn.commit()
    conn.close
