#todo: Сделать рефакторинг кода задачи task1  22 лекции .
#  1. Реализовать из класса DB синглтон. Экземляр класса(подключение) должно быть единственным.
#  2. Реализовать  фабрику которая создает модели различных производителей
# 3. Реализовать для класса Car абстрактный класс который содержит
# aбстрактные методы sold, discount

from abc import ABC, abstractmethod

class AbsCar(ABC):

    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass

class Car(AbsCar):

    def __init__(self, brand, model):
        seld.brandt = brand
        self.model = model

    @classmethod
    def make_toyota(cls):
        return cls("Toyota", "Camry")

    @classmethod
    def make_wolksvagen(cls):
        return cls("Wolksvagen", "Polo")

    @classmethod
    def make_ford(cls):
        return cls("Ford", "Focus")

    def sold(self):
        print(f"Поздравляем! Вы купили автомобиль {self.brand} {self.model}!")

    def discount(self):
        sale = input("Введите процент скидки:")
        print(f"На автомобиль {self.brand} {self.model} действует скидка {sale}%.")
