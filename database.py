#Creating sql data base

import sqlite3
import pandas as pd


# Define the path to SQLite database file and the CSV file
database_path = 'BooksTable.db'
csv_file = '/Users/chideravictor/Desktop/Bookshop/BooksTable.csv'

#Connect to SQLite datavase
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Drop the table if it exists to avoid schema issues
cursor.execute("DROP TABLE IF EXISTS books")

# Load CSV data into a DataFrame
df = pd.read_csv(csv_file)

# Insert data into the 'books' table
df.to_sql('bookstable', conn, if_exists='replace', index=False)

# Save changes
conn.commit()

# Close connection
conn.close()