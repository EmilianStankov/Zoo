import sqlite3


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
