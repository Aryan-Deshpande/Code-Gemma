
import sqlite3

conn = sqlite3.connect('text_storage.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS texts
                 (id INTEGER PRIMARY KEY, text TEXT)''')

def insert_text(text):
    cursor.execute("INSERT INTO texts (text) VALUES (?)", (text,))
    conn.commit()
    print("Text inserted successfully.")

def fetch_all_texts():
    cursor.execute("SELECT * FROM texts")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    text_to_insert = input("Enter text to insert into the database: ")
    insert_text(text_to_insert)

    print("\nAll texts in the database:")
    fetch_all_texts()

conn.close()
