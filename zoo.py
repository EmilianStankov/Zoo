import sqlite3
from class_animal import Animal


class Zoo():
    def __init__(self, animals, capacity, budget, name):
        self._animals = animals
        self._capacity = capacity
        self._budget = budget
        self._name = name

    def get_animals(self):
        return self._animals

    def get_capacity(self):
        return self._capacity

    def get_budget(self):
        return self._budget

    def get_name(self):
        return self._name

    def save(self):
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS zoos
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, name)""")
        query = ("INSERT INTO zoos(name) VALUES(?)")
        data = [self.get_name()]
        cursor.execute(query, data)
        db.commit()
        db.close()

    def daily_income(self):
        __income = 0
        for animal in self._animals:
            __income += 60
        return __income

    def accomodate(self, animal):
        self._animal = animal
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        query = ("SELECT id FROM zoos WHERE name = ?")
        data = [self.get_name()]
        for line in cursor.execute(query, data):
            zoo_id = line[0]
        cursor.execute("""CREATE TABLE IF NOT EXISTS animals_in_zoo
                          (zoo_id, species, name, status, gender,
                           unique_animal_id INTEGER PRIMARY KEY AUTOINCREMENT)
                       """)
        query = ("""INSERT INTO animals_in_zoo(zoo_id, species,
                                               name, status, gender)
                    VALUES(?, ?, ?, ?, ?)""")
        data = [zoo_id, self._animal.get_species(),
                self._animal.get_name(), self._animal.get_status(),
                self._animal.get_gender()]
        cursor.execute(query, data)
        db.commit()
        db.close()

    def daily_outcome(self):
        __outcome = 0
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        for animal in self._animals:
            __weight = animal.get_weight()
            __species = animal.get_species()
            query = ("""SELECT food_type, food_weight_ratio
                        FROM animals WHERE species = ?""")
            data = [__species]
            for line in cursor.execute(query, data):
                type_of_food = line[0]
                food_weight_ratio = line[1]
            if type_of_food == 'carnivore':
                __outcome += 4 * __weight * food_weight_ratio
            else:
                __outcome += 2 * __weight * food_weight_ratio

        return int(__outcome)


lion = Animal('lion', 2, 'Pesho', 'male', 100)
zoo = Zoo([lion], 10, 1000, 'Zoo')
zoo.daily_outcome()
