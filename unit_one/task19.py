#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
#"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.

import csv

file = "algoritm.csv"
f = open("algoritm.csv", mode = "tw", encoding = "UTF-8")

algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
id = 1

for i in alrogitm:
    f.write(str(id) + ". " + i + "\n")
    id = id + 1

writer = csv.writer(f)
writer.writerows(zip(algoritm,id))
f.close()
