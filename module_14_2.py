import sqlite3

# Создание базы данных и подключение к ней
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
connection.commit()

# Создание таблицы, если её ещё нет
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
""")
connection.commit()  # Подтверждение изменений
# Наполнение таблицы данными
insert_data_query = """ 
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
"""

data_list = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]

cursor.executemany(insert_data_query, data_list)

connection.commit()  # Подтверждение изменений


#Обновление баланса на 500 каждого 2 пользователя начиная с1
cursor.execute('UPDATE Users SET balance = 500 WHERE id IN (SELECT id FROM Users WHERE id % 2 = 1)')
connection.commit()  # Подтверждение изменений

#Удаление каждой 3ей записи  в таблице начиная с 1ой:
cursor.execute("""
DELETE FROM Users
WHERE id IN (SELECT id FROM Users WHERE id % 3 = 1)
""")
connection.commit()  # Подтверждение изменений

# Вывод в консоль всех пользователей возраст которых не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit() # Подтверждение изменений

cursor.execute("""
DELETE FROM Users
WHERE id = 6
""")
connection.commit()  # Подтверждение изменений
# connection.close() # Закрытие подключения

# Подсчёт общего количества записей
cursor.execute("""
SELECT COUNT(*) as record_count
FROM Users
""")
connection.commit()  # Подтверждение изменений

total_records = cursor.fetchone()
total_users = total_records[0] if total_records else 0

print(f"Общее количество записей: {total_users}")

 # Посчитаем сумму всех балансов
sum_balances_query = """
SELECT SUM(balance) as total_balance
FROM Users
"""

cursor.execute(sum_balances_query)
total_balance = cursor.fetchone()
all_balances = total_balance[0] if total_balance else 0

print(f"Сумма всех балансов: {all_balances}")

# Вычисление и вывод среднего баланса
average_balance_query = """
SELECT AVG(balance) as average_balance
FROM Users
"""
connection.commit()

cursor.execute(average_balance_query)
average_balance = cursor.fetchone()
avg_balance = average_balance[0] if average_balance else 0.0
print(f"Средний баланс всех пользователей: {avg_balance}")
connection.commit() # Подтверждение изменений
connection.close()

