import unittest
from zoo import Zoo
from class_animal import Animal


class ZooTests(unittest.TestCase):
    def setUp(self):
        self.tiger = Animal('tiger', 2, 'Pesho', 'male', 100)
        self.lion = Animal('lion', 5, 'Gosho', 'female', 120)
        self.male_lion = Animal('lion', 3, 'Petko', 'male', 100)
        self.goat = Animal('goat', 3, 'Kolio', 'male', 80)
        self.zoo = Zoo([self.tiger, self.lion,
                        self.goat, self.male_lion], 1000, 100000, 'Zoo')

    def test_zoo_get_animals(self):
        self.assertEqual([self.tiger, self.lion, self.goat, self.male_lion],
                         self.zoo.get_animals())

    def test_zoo_get_capacity(self):
        self.assertEqual(1000, self.zoo.get_capacity())

    def test_zoo_get_budget(self):
        self.assertEqual(100000, self.zoo.get_budget())

    def test_zoo_get_name(self):
        self.assertEqual('Zoo', self.zoo.get_name())

    def test_zoo_save(self):
        self.zoo.save()

    def test_zoo_income(self):
        self.assertEqual(240, self.zoo.daily_income())

    def test_accomodate(self):
        self.zoo.accomodate(self.tiger)
        self.zoo.accomodate(self.lion)
        self.zoo.accomodate(self.goat)
        self.zoo.accomodate(self.male_lion)

    def test_daily_outcome(self):
        self.assertEqual(115, self.zoo.daily_outcome())

    def test_simulate_period_of_time(self):
        self.zoo.simulate_time('months', 10)
        self.assertEqual(137500, self.zoo.get_budget())


if __name__ == '__main__':
    unittest.main()
