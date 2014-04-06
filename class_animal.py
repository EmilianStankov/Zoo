import sqlite3
import random


class Animal():
    """docstring for Animal"""
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.conn = sqlite3.connect("animals.db")
        self.animal = self.conn.cursor()
        self.status = True
        self.all_database_by_species(self.species)

    def all_database_by_species(self, species):
        query_animals = ("SELECT * FROM animals WHERE species=?")
        data_animals = [self.species]
        row = self.animal.execute(query_animals, data_animals)
        for item in row:
            self.life_expectancy = item[1]
            self.food_type = item[2]
            self.gestation_period = item[3]
            self.newborn_weight = item[4]
            self.average_weight = item[5]
            self.weight_age_ratio = item[6]
            self.food_weight_ratio = item[7]

    def get_species(self):
        return self.species

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_weight(self):
        return self.weight

    def grow_animal(self, period_of_time):
        if self.age < self.life_expectancy:
            if self.weight < self.average_weight:
                self.weight += self.weight_age_ratio * period_of_time
                self.age += period_of_time / 12
            else:
                self.age += period_of_time / 12
        else:
            self.status = False

    def eat(self):
        return self.food_weight_ratio * self.weight

    def chance(self):
        chance_to_live = (self.age / self.life_expectancy) * 100
        random_number = random.uniform(0, 100)
        if random_number <= chance_to_live:
            self.status = False
        self.status = True

    def get_status(self):
        return self.status

#new_animal = Animal('lion', 2, 'gosho', 'male', 10)
#new_animal.all_database_by_speaceis('lion')
