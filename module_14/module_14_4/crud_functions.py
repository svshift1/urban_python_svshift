import sqlite3

sql_createtable = '''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY, 
            title text NOT NULL,
            description test NOTT NULL,
            price  INTEGER NOT NULL) '''


def initiate_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(sql_createtable)
    cur.execute("SELECT count(*) FROM products")
    count = cur.fetchone()[0]
    if count == 0:
        for x in "ABCDE":
            el = (f"Витамин {x}", f"Описание Витамина {x}", (ord(x) - 64) * 50)  # (title, description, price)
            cur.execute('INSERT INTO products (title,description,price) VALUES (?, ?, ?)', el)
        conn.commit()


def get_all_products(conn: sqlite3.Connection) -> list:
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, price FROM products ORDER BY id")
    prods = cur.fetchall()
    prods = [dict(zip(('id', 'title', 'description', 'price'), p)) for p in prods]
    return prods
