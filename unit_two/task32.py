# todo: Реализовать класс "Игровой персонаж".
#  Класс должен содержать атрибуты(свойства): Идентификатор, Имя, Здоровье, Раса, Тип персонажа, урон.
#  Инициализация атрибутов(состояние объекта) должна происходить в конструкторе.
#  В классе реализовать метод изменения здоровья по нанесенному урону(параметр функции).
#  Заложить логику: При достижении порога здоровья персонаж погибает
#  В классе реализовать метод получения значения атрибута урона
#  При достижении порога здоровья персонаж погибает
#  Реализовать дандер __repr__ для отладки персонажа
#  Реализовать дандер вычитания __sub__()  написав логику "боя" которая срабатывает
#  в момент вычитания объектов класса obj1 - obj2 и заключается в вычитании из
#  здоровья первого объекта урона наносимого вторым объектом

class Character:

    def __init__(self, id, name, health, race, character_type, damage):
        self.id: int = id
        self.name: str = name
        self.health: int = health
        self.race: str = race
        self.character_type: str = character_type
        self.damage: int = damage

    def __sub__(self, enemy):
        self.health -= enemy.damage
        if self.health <= 0:
            print(f"Увы {self.name} пал в честном бою!")

    def __repr__(self):
        return f"Персонаж по имени {self.name}, имеет идентификационный номер {self.id},
        раса этого персонажа – {self.race}, тип этого персонажа – {self.character_type},
        его уровень здоровья равен {self.health}, он наносит урон равный {self.damage}."
