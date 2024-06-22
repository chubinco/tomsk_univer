import sqlite3
from random import randint


def create_db_table_athletes():

    connect = sqlite3.connect("./sportsmens.db")
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Athletes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT,
    sport TEXT
    );
    ''')


def add_athletes(list_athletes):
    query = '''INSERT INTO Athletes (name, gender, age, country, sport) VALUES (?, ?, ?, ?, ?);'''
    try:
        with sqlite3.connect("./sportsmens.db") as conn:
            cursor = conn.cursor()
            cursor.executemany(query, list_athletes)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def list_athletes():
    query = '''SELECT * FROM Athletes;'''
    try:
        with sqlite3.connect("./sportsmens.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            lst = cursor.fetchall()
            print(f'\nСписок спортсменов из таблицы "Athletes"')
            print("=" * 39)
            for athlete in lst:
                print(f'Спортсмен: {athlete[1]}\nСтрана: {athlete[4]}\nВид спорта: {athlete[5]}\n'
                      f'Возраст: {athlete[3]} лет/года\nПол: {athlete[2]}')
                print("-" * 30)
            return lst
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    f


def user_input_athletes():
    lst_athletes = []
    while True:
        flag = input('Продолжаем заполнять таблицу? (Да/Нет) ')
        if flag.lower() == 'нет':
            break
        athlete = []
        questions = [
            'Как зовут Вашего любимого спортсмена? ',
            'Он мужчина или женщина? ',
            'Его возраст: ',
            'Из какой он страны: ',
            'В каком виде спорта он достиг успеха? '
        ]
        for question in questions:
            athlete.append((input(question)).strip())
        lst_athletes.append(tuple(athlete))
    add_athletes(lst_athletes)


def insert_column():
    query = 'ALTER TABLE Athletes ADD COLUMN action INTEGER;'
    sql = 'SELECT * FROM Athletes;'
    try:
        with sqlite3.connect("./sportsmens.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            cursor.execute(sql)
            lst = cursor.fetchall()
            name_columns = cursor.description
            columns_db = []
            for row in name_columns:
                columns_db.append(row[0])
            print(f'Имена колонок в таблице "Athletes"\n{columns_db}\n')
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_action_random():
    query = 'SELECT * FROM Athletes;'
    query_update = 'UPDATE Athletes SET action = ? WHERE id = ?'
    try:
        with sqlite3.connect("./sportsmens.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            list_db = cursor.fetchall()
            for row in list_db:
                num = randint(0, 1)
                id_row = int(row[0])
                cursor.execute(query_update, (num, id_row))
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def action_selection():
    query = 'SELECT COUNT(*), action FROM Athletes GROUP BY action;'
    try:
        with sqlite3.connect('./sportsmens.db') as conn:
            cur = conn.cursor()
            cur.execute(query)
            set = cur.fetchall()
            print(
                f'В таблице представлено:\n {set[1][0]} действующих спортсменов;\n {set[0][0]} недействующих спортсменов;')
            conn.commit()
    except sqlite3.Error as e:
        print(e)


def action_select_to_delete():
    query_del = 'DELETE FROM Athletes WHERE id IN (SELECT id FROM Athletes WHERE action = 0);'
    try:
        with sqlite3.connect('./sportsmens.db') as conn:
            cur = conn.cursor()
            cur.execute(query_del)
            conn.commit()
    except sqlite3.Error as e:
        print(e)


athletes = [
    ('Александр Овечкин', 'мужчина', '38', 'Россия', 'хоккей'),
    ('Мария Шарапова', 'женщина', 37, 'Россия', 'теннис'),
    ('Lionel Messi', 'мужчина', 36, 'Аргентина', 'футбол'),
    ('Елена Вяльбе', 'женщина', 56, 'Россия', 'лыжные гонки'),
    ('Max Verstappen', 'мужчина', 26, 'Бельгия', 'формула 1'),
    ('Novak Djokovic', 'мужчина', 37, 'Сербия', 'теннис'),
    ('Екатерина Гамова', 'женщина', 43, 'Россия', 'воллейбол'),
    ('Александр Большунов', 'мужчина', 27, 'Россия', 'лыжные гонки')
]
# ('Алексей Немов', 'мужчина', 48, 'Россия', 'гимнастика')

create_db_table_athletes()
add_athletes(athletes)
user_input_athletes()
list_athletes()
insert_column()
update_action_random()
action_selection()
action_select_to_delete()
list_athletes()

