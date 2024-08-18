import sqlite3

# Define the path to the SQLite database file
database_path = '/Users/chideravictor/Desktop/Bookshop/BooksTable.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Query the schema of the 'books' table
cursor.execute("PRAGMA table_info(books);")
schema = cursor.fetchall()

print("Table Schema:")
for column in schema:
    print(column)

# Query the contents of the 'books' table
cursor.execute("SELECT * FROM books LIMIT 10;")
rows = cursor.fetchall()

print("\nTable Data:")
for row in rows:
    print(row)

# Close the connection
conn.close()
