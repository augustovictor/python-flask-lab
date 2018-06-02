import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# USERS
create_table = """CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(30),
    password VARCHAR(55)
)"""

cursor.execute(create_table)

users = [
    ('victor', '123123'),
    ('rotciv', '321321'),
]

inser_query = "INSERT INTO users (username, password) VALUES(?, ?)"

cursor.executemany(inser_query, users)
select_query = 'SELECT * FROM users'

for row in cursor.execute(select_query):
    print(row)

# ITEMS
createItemsQuery = """
    CREATE TABLE items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        price DECIMAL(5,2) NOT NULL DEFAULT 0.00
    )
"""

itemsFixture = [
    ('item1', 20.90),
    ('item2', 10.23),
    ('item3', 93.19)
]

cursor.execute(createItemsQuery)

insert_query = 'INSERT INTO items (name, price) VALUES(?, ?)'
cursor.executemany(insert_query, itemsFixture)

connection.commit()
connection.close()
