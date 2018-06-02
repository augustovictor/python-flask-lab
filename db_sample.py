import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = """CREATE TABLE users (
    id INTEGER(11) NOT NULL,
    username VARCHAR(30),
    password VARCHAR(55)
)"""

cursor.execute(create_table)

users = [
    (1, 'victor', '123123'),
    (2, 'rotciv', '321321'),
]

inser_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.executemany(inser_query, users)
connection.commit()

select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

connection.close()
