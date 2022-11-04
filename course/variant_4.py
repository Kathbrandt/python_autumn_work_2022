#БД «Кондитерская фабрика»
#Описание предметной области. БД создается для информационного обслуживания администрации фабрики. Фабрика изготавливает кондитерские изделия. Для изготовления товара требуются продукты, которые фабрика заказывает у поставщиков. Готовые товары расфасовываются для магазинов.
#Готовые запросы:
#1. Показывать список магазинов, заказывающих данный товар;
#2. Показывать список продуктов, заказываемых у данного поставщика;
#3. Показывать ассортимент данного товара и цену;
#4. Выбирать наиболее популярный вид данного товара

import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "candy_factory",
    user = "postgres",
    password = "210998"
);

cursor = connection.cursor()

#1. Показывать список магазинов, заказывающих данный товар;
print("Наши вкуснейшие корзиночки заказывают такие заведения, как:")

SQL_ALL_BUYERS = f"""SELECT title
                     FROM buyer"""

cursor.execute(SQL_ALL_BUYERS)

shops = cursor.fetchall()

for row in shops:
    print(row)

print()

#2. Показывать список продуктов, заказываемых у данного поставщика;

print("Список продуктов, заказываемых у одного поставщика.")

suppleir = input("Введите id поставщика:")

SQL_INGREDIENTS_FROM_PROVIDER = f"""SELECT tittle
                                    FROM ingredient
                                    WHERE fk_provider_id = '{supplier}'"""

cursor.execute(SQL_INGREDIENTS_FROM_PROVIDER)

ing_titles = cursor.fetchall()

for row in ing_titles:
    print(ing_titles)

print()

#3. Показывать ассортимент данного товара и цену;

print("Вот все наши корзиночки и цены на них:")

SQL_ALL_PRODUCTS_AND_PRICES = f"""SELECT title, price
                             FROM products"""

cursor.execute(SQL_ALL_PRODUCTS_AND_PRICES)

product_and_price = cursor.fetchall()

for row in product_and_price:
    print(row[0], "стоит", row[1], "рублей")

print()

#4. Выбирать наиболее популярный вид данного товара

SQL_MOST_POPULAR_PRODUCT_ID = f"""SELECT product_id, COUNT(product_id) AS "most_pop"
                               FROM buyer_product
                               GROUP BY product_id
                               ODER BY "most_pop" DESC
                               LIMIT 1 """

cursor.execute(SQL_MOST_POPULAR_PRODUCT_ID)

most_popular_id = cursor.fetchall()

SQL_MOST_POPULAR_PRODUCT_NAME = f"""SELECT title
                                    FROM product
                                    WHERE product_id = '{most_popular_id}'"""

cursor.execute(SQL_MOST_POPULAR_PRODUCT_NAME)

most_popular_name = cursor.fetchall()

print(most_popular_name, "– наш самый популярный продукт, ее заказывает наибольшее количество поставщиков!")
print()

connection.close()
