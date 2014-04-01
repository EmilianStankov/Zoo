import unittest
from zoo import Zoo


class ZooTests(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo(['tiger', 'lion', 'hippo'], 1000, 100000, 'Zoo')

    def test_zoo_get_animals(self):
        self.assertEqual(['tiger', 'lion', 'hippo'], self.zoo.get_animals())

    def test_zoo_get_capacity(self):
        self.assertEqual(1000, self.zoo.get_capacity())

    def test_zoo_get_budget(self):
        self.assertEqual(100000, self.zoo.get_budget())

    def test_zoo_get_name(self):
        self.assertEqual('Zoo', self.zoo.get_name())

    @unittest.skip("Skip this.")
    def test_zoo_save(self):
        self.zoo.save()

    def test_zoo_income(self):
        self.assertEqual(180, self.zoo.daily_income())


if __name__ == '__main__':
    unittest.main()
