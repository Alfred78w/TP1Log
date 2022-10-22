import unittest


class TestWeapon(unittest.TestCase):
    def test_range(self):
        distance = distance()
        result = (range>=distance)
        self.assertEqual(True, result)  # add assertion here

    def test_ammunition(self):
        ori = Weapon.ammunitions
        self.assertEqual()
if __name__ == '__main__':
    unittest.main()
