import sqlite3

conn = sqlite3.connect('shop.db')

c = conn.cursor()

# Create table for products
c.execute('''
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        photo_url TEXT,
        description TEXT
    )
''')

# Create table for carts
c.execute('''
    CREATE TABLE carts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

conn.commit()

conn.close()

