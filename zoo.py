import sqlite3
import random
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
        name_not_taken = True
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS zoos
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name, budget)""")
        for line in cursor.execute("SELECT name FROM zoos"):
            if line[0] != self.get_name():
                name_not_taken = True
            else:
                name_not_taken = False
                break
        if name_not_taken:
            query = ("INSERT INTO zoos(name, budget) VALUES(?, ?)")
            data = [self.get_name(), self.get_budget()]
            cursor.execute(query, data)
            db.commit()
            db.close()
        else:
            print("A zoo with this name already exists!")

    def daily_income(self):
        __income = 0
        for animal in self._animals:
            __income += 60
        return __income

    def accomodate(self, animal):
        self._animal = animal
        not_in_zoo = True
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        query = ("SELECT id FROM zoos WHERE name = ?")
        data = [self.get_name()]
        for line in cursor.execute(query, data):
            zoo_id = line[0]
        cursor.execute("""CREATE TABLE IF NOT EXISTS animals_in_zoo
                          (zoo_id, species, name, status, gender,
                           gestation_period, weight, age,
                           unique_animal_id INTEGER PRIMARY KEY AUTOINCREMENT)
                       """)
        animals_in_zoo = cursor.execute("""SELECT species, name
                                           FROM animals_in_zoo""")

        for animal in animals_in_zoo:
            if (self._animal.get_species(), self._animal.get_name()) != animal:
                not_in_zoo = True
            else:
                not_in_zoo = False
                break

        if not_in_zoo:
            if self._animal.get_gender() == 'male':
                _gestation_period = 0
            else:
                _gestation_period = self._animal.gestation_period

            query = ("""INSERT INTO animals_in_zoo(zoo_id, species,name,
                        status, gender, gestation_period, weight, age)
                        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""")
            data = [zoo_id, self._animal.get_species(),
                    self._animal.get_name(), self._animal.get_status(),
                    self._animal.get_gender(), _gestation_period,
                    self._animal.get_weight(), self._animal.get_age()]
            cursor.execute(query, data)
            db.commit()
            db.close()
        else:
            print('Animal from this species with the same name is in the zoo!')

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

    def simulate_time(self, interval, period):
        db = sqlite3.connect("animals.db")
        cursor = db.cursor()
        query = ("SELECT id FROM zoos WHERE name = ?")
        data = [self.get_name()]
        for line in cursor.execute(query, data):
            __zoo_id = line[0]
        if interval == 'days':
            __period = period
        elif interval == 'weeks':
            __period = period * 7
        elif interval == 'months':
            __period = period * 30
        elif interval == 'years':
            __period = period * 365
        for i in range(__period):
            self._budget += self.daily_income()
            self._budget -= self.daily_outcome()
        query = ("UPDATE zoos SET budget = ?")
        data = [self.get_budget()]
        cursor.execute(query, data)
        db.commit()
        for animal in self._animals:
            newborn_gender = ''
            __species = animal.get_species()
            if animal.get_gender() == 'male':
                for other_animal in self._animals:
                    if (other_animal.get_gender() == 'female'
                       and animal.get_species() == other_animal.get_species()):
                        other_animal.gestation_period -= __period / 30
                        if other_animal.gestation_period <= 0:
                            other_animal.gestation_period = 0
                        if random.choice([True, False]):
                            newborn_gender = 'male'
                        else:
                            newborn_gender = 'female'
                        query = ("""UPDATE animals_in_zoo
                                    SET gestation_period = ?
                                    WHERE zoo_id = ? AND species = ?""")
                        data = [other_animal.gestation_period,
                                __zoo_id, __species]
                        self.accomodate(Animal(animal.get_species(), 0,
                                               'Goshko', newborn_gender,
                                               animal.newborn_weight))
                        self._animals.append(Animal(animal.get_species(), 0,
                                                    'Goshko', newborn_gender,
                                                    animal.newborn_weight))
                        break
            animal.grow_animal(__period / 30)
            if animal.get_weight() >= animal.average_weight:
                animal.weight = animal.average_weight
            query = ("""UPDATE animals_in_zoo
                        SET age = ?, weight = ?, status = ?
                        WHERE zoo_id = ? AND species = ?""")
            data = [animal.get_age(), animal.get_weight(), animal.get_status(),
                    __zoo_id, __species]
            cursor.execute(query, data)
            db.commit()
        db.close()
