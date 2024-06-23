import sqlite3

# Create tables from this file, add the name of the table just after the underscore

def create_table_():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS "" (
        );
    ''')
    conn.commit()
    conn.close()

#'''
## Example:

#def create_table_users():
    #conn = sqlite3.connect('data.db')
    #cursor = conn.cursor()
    #cursor.execute('''
        #CREATE TABLE IF NOT EXISTS "utenti" (
            #"id" INTEGER NOT NULL,
            #"email" TEXT NOT NULL UNIQUE,
            #"user_type" TEXT NON NULL,
            #"password" TEXT NOT NULL,
            #PRIMARY KEY("id")
        #)
    #''')
    #conn.commit()
    #conn.close()
#'''
