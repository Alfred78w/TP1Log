import unittest


class TestWeapon(unittest.TestCase):
    def test_ammunition(self, weapon):
        ori = weapon.ammunitions
        weapon.fire_at(0,0,0)
        end = weapon.ammunitions
        self.assertEqual(ori-1, end)

if __name__ == '__main__':
    unittest.main()
