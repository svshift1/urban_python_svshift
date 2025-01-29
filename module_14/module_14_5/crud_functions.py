import sqlite3


def initiate_db(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()

    # products
    sql_create_product_table = '''CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY, 
                title text NOT NULL,
                description test NOTT NULL,
                price  INTEGER NOT NULL) '''
    cur.execute(sql_create_product_table)
    cur.execute("SELECT count(*) FROM products")
    count = cur.fetchone()[0]
    if count == 0:
        for x in "ABCDE":
            el = (f"Витамин {x}", f"Описание Витамина {x}", (ord(x) - 64) * 50)  # (title, description, price)
            cur.execute('INSERT INTO products (title,description,price) VALUES (?, ?, ?)', el)
        conn.commit()

    # users
    sql_create_users_table = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY, 
                username text NOT NULL,
                email test NOTT NULL,
                age  INTEGER NOT NULL,
                balance INTEGER NOT NULL) '''
    cur.execute(sql_create_users_table)
    # cur.execute("SELECT count(*) FROM users")
    # count = cur.fetchone()[0]
    # if count == 0:
    #     for i in range(1, 11):
    #         cur.execute('INSERT INTO users (username, email, age, balance) VALUES (?,?,?,?)',
    #                     (f'User{i}', f'example{i}.gmail.com', i * 10, 1000))


def get_all_products(conn: sqlite3.Connection) -> list:
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, price FROM products ORDER BY id")
    prods = cur.fetchall()
    prods = [dict(zip(('id', 'title', 'description', 'price'), p)) for p in prods]
    return prods


def add_user(conn: sqlite3.Connection, username: str, email: str, age: int) -> None:
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, email, age, balance) VALUES (?,?,?,?)',
                (username, email, age, 1000))
    conn.commit()


def is_included(conn: sqlite3.Connection, username: str) -> bool:
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM users WHERE username = ?", (username,))
    res = cur.fetchone()[0]
    return res > 0
