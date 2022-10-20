#todo: Взлом шифра
#Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
#Попробуйте все возможные сдвиги и расшифруйте фразу.
#grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin"

letters_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_down = letters_up.lower()

for num in range (1, len(letters_down) + 1):
    list = []
    for i in text:
        if i in letters_down:
            list.append(letters_down[letters_down.index(i) - num])
        else:
            list.append(i)
    print(num, " ".join(list))
