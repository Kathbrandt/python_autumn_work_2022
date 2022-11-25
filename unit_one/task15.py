# # Написать игру "Поле чудес"
#
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

from random import randint

words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования",
"Состав и взаимное расположение частей какого-н. строения, сооружения, механизма, а также само строение, сооружение",
"Сущность в цифровом пространстве, обладающая состоянием и поведением, имеющая поля и методы"]

random_word = randint(0, 2)
print(desc_[random_word])
word = words[random_word]

template = ["▒" for in word]
print("".join(template), "В этом слове", len(word), "букв.")

possible_mistakes = 10
mistakes_made = 0

while word != "".join(template):

    letter = str(input("Введите одну букву, которая, по вашему мнению, есть в слове:"))

    if letter not in word:
        mistakes_made += 1
        if mistakes_made == possible_mistakes:
            print("У вас больше не осталось попыток, чтобы угадать слово!")
            break
        else:
            print(f"Такой буквы нет в слове:( \n У вас осталось {possible_mistakes-mistakes_made} попыток")
            continue

    if letter in word:
        start = 0
        for x in range(list(word).count(letter)):
            ind = list(word).index(letter,start,len(secret))
            start = ind + 1
            tamplate[ind] = letter

if mistakes_made < 10:
    print("".join(template))
     print('Поздравляю! Вы отгадали слово!')
