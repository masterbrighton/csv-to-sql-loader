import pandas as pd
import sqlite3

# load the csv
df = pd.read_csv("data/sample_data.csv")


# clean the data (drop rows with missing data (age))
df_clean = df.dropna(subset=["age"])


# connect to SQLite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
       name TEXT,
       email TEXT,
       age INTEGER,
       signup_date TEXT
)
''')

# insert the data
df_clean.to_sql("users", conn, if_exists="replace", index=False)

# run a query
cursor.execute("SELECT * FROM USERS")
rows = cursor.fetchall()
for row in rows:
    print(row)

# close the connection
conn.close()