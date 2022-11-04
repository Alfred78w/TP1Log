import unittest
import Weapon as wp


class MyTestCase(unittest.TestCase):
    def test_lance_torpilles(self):
        c = wp.Lance_torpilles()
        try:
            c.fire_at(2, 3, 1)
        except wp.Range_Munition as exc:

            print("erreur, message :", exc)

        except wp.NoAmmunitionError as exc:
            print("erreur, message :", exc)

        except wp.OutOfRangeError as exc:
            print("erreur, message :", exc)

            print(c)  # normalement on doit avoir 14 munitions car le z est négatif

            self.assertEqual(14, c.ammunition)


if __name__ == '__main__':
    unittest.main()
