from aiogram import yes
import sqlite3

def add_product(name, price, category, image):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (name, price, category, image) VALUES (?, ?, ?, ?)", (name, price, category, image))
    conn.commit()
    conn.close()

def edit_product(id, name, price, category, image):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("UPDATE products SET name = ?, price = ?, category = ?, image = ? WHERE id = ?", (name, price, category, image, id))
    conn.commit()
    conn.close()

def remove_product(id):
    conn = sqlite3.connect('shop.db')
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()
    conn.close()
