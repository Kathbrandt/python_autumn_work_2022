#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}
quantity = {
 "banana": 6,
 "apple": 8,
 "orange": 3,
 "pear": 5
}

def compute_bill(prices_dict, quantity_dict):
    bill_sum = 0
    for x in price_dict.keys():
        bill_sum = prices_dict[x]*quantity_dict[x]
    return bill_sum

print(compute_bill(prices,quantity))
