import os
import sqlite3

DB_FILENAME = 'not_telegram.db'
# скрипты
sql_createtable = '''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            username text NOT NULL,
            email test NOTT NULL,
            age  INTEGER NOT NULL,
            balance INTEGER NOT NULL) '''

# создадим .bd или перезапишем существующий
try:
    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)  # DROP DATABASE IF EXISTS )))
    # чтобы в случае аварии или успеха база автомагически закрывалась
    with sqlite3.connect(DB_FILENAME) as conn:
        cur = conn.cursor()

        # создаем таблицу
        cur.execute(sql_createtable)

        # вставляем данные
        for i in range(1, 11):
            cur.execute('INSERT INTO users (username, email, age, balance) VALUES (?,?,?,?)',
                        (f'User{i}', f'example{i}.gmail.com', i * 10, 1000))

        # обновляем каждого второго юзера
        for i in range(1, 11, 2):
            cur.execute('UPDATE users SET balance = ? WHERE username=?',
                        (500, f'User{i}'))

        # удаляем каждую 3ю запись
        for i in range(1, 11, 3):
            cur.execute('DELETE FROM users WHERE username=?', (f'User{i}',))

        # выборка
        cur.execute('SELECT username, email, age, balance FROM users WHERE age != ?', (60,))
        for user in cur.fetchall():
            print("Имя: %s | Почта: %s | Возраст: %d | Баланс: %d " % user)

except Exception as e:
    print("Error with DB:", e)
