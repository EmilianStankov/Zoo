import unittest
import class_animal
import functools


class AnimalTest(unittest.TestCase):
    """docstring for AnimalTests"""
    def setUp(self):
        self.new_animal = class_animal.Animal('lion', 2, 'gosho', 'male', 10)
        self.new_animal.all_database_by_speaceis(self.new_animal.get_species())
        self.new_animal1 = class_animal.Animal('lion', 15, 'pesho', 'male', 20)
        self.new_animal1.all_database_by_speaceis(self.new_animal1.get_species())
        self.new_animal2 = class_animal.Animal('lion', 5, 'mila', 'female', 210)
        self.new_animal2.all_database_by_speaceis(self.new_animal2.get_species())

    def test_get_species(self):
        self.assertEqual("lion", self.new_animal.get_species())

    def test_get_age(self):
        self.assertEqual(730, self.new_animal.get_age())

    def test_get_name(self):
        self.assertEqual('gosho', self.new_animal.get_name())

    def test_get_gender(self):
        self.assertEqual('male', self.new_animal.get_gender())

    def test_get_weight(self):
        self.assertEqual(10, self.new_animal.get_weight())

    def test_get_status(self):
        self.assertTrue(self.new_animal.get_status())

    def test_eat(self):
        self.assertEqual(0.035 * self.new_animal.get_weight(), self.new_animal.eat())

    def test_grow_animal_for_animal1(self):
        self.assertTrue(not self.new_animal1.grow_animal(1))

    def test_grow_animal_for_animal2(self):
        self.assertEqual(self.new_animal2.get_age() + 2, self.new_animal2.grow_animal(2))

    def test_grow_animal_for_animal(self):
        self.assertEqual((self.new_animal.get_age() + 2, 17.5), self.new_animal.grow_animal(2))

    def test_chance(self):
        result = []
        for age in range(self.new_animal.life_expectancy):
            result.append(self.new_animal.chance(age))
        self.assertTrue(functools.reduce(lambda a, b: a or b, result))


if __name__ == '__main__':
    unittest.main()
