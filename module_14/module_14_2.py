import sqlite3

import module_14_1 # запуск предыдущего

DB_FILENAME = 'not_telegram.db'

try:
    with sqlite3.connect(DB_FILENAME) as conn:
        cur = conn.cursor()

        # удаление id=6
        cur.execute('DELETE FROM users where id=6')

        # к-во записей
        cur.execute('SELECT count(*) FROM users')
        #count = cur.fetchone()[0]
        count = cur.fetchall()[0][0]  # у вас ошибка в тексте лекции ! у вас там fetchall делается после fetchone
        print(f'Всего записей {count}')

        # сумма
        cur.execute('SELECT sum(balance) FROM users')
        sumbalance = cur.fetchone()[0]
        print(f"Сумммарный баланс: {sumbalance}")

        # cur.execute('SELECT avg(balance) FROM users') # а почему не так?
        # avgbalance = cur.fetchone()[0]
        avgbalance = sumbalance/count
        print(f"Средний баланс: {avgbalance}")





except Exception as e:
    print("Error with DB:", e)
