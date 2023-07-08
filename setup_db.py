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
        description TEXT,
        quantity INTEGER NOT NULL
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

# Create table for users
c.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER NOT NULL,
        role TEXT NOT NULL
    )
''')

# Create table for FAQs
c.execute('''
    CREATE TABLE faqs (
        id INTEGER PRIMARY KEY,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

# Create table for About
c.execute('''
    CREATE TABLE about (
        id INTEGER PRIMARY KEY,
        content TEXT NOT NULL
    )
''')

# Create table for DeliveryMethod
c.execute('''
    CREATE TABLE delivery_methods (
        id INTEGER PRIMARY KEY,
        content TEXT NOT NULL
    )
''')

conn.commit()

conn.close()

