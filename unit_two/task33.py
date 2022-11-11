# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

#  1. пользователь ввел некорректное значение в заданном диапазоне
class MyValueErrorException(ValueError):
    print("Вы ввели некорректное значение. Значение должно быть больше нуля.")

def validate(value):
    if len(value) < 0:
        raise MyValueErrorException()

#  2. результат запроса вернул 0 строк

class NullResultException(Exception):
    print("Такого объекта не существует.")

import psycopg2

connection = psycopg2.connect(
host = "localhost",
database = "candy_factory",
user = "postgres",
password = "210998");

cur = connection.cursor()

SQL_ROW_SELECTION = f"""SELECT name
                            FROM column
                            WHERE id = 5"""
cur.execute(SQL_ROW_SELECTION)

result = cur.fetchall()

if result = NULL:
    raise NullResultException()

#  3. Произошел разрыв соединения с сервером
class MyConnectionResetErrorException(ConnectionResetError):
    print("Произошел разрыв соединения с сервером.")

def connection_validation():
    connection = psycopg2.connect(
    host = "localhost",
    database = "candy_factory",
    user = "postgres",
    password = "210998");

    if ConnectionResetError:
        raise MyConnectionResetErrorException()

# Извиняюсь, если этот код причинил вам боль и моральные страдания
