import unittest
import Weapon as wp

""" Danc ce test, si le nombre de munition est nulle, l'on obteint un message d'erreur lors de l'éxécuti"""
"""De même, si le z est nnégatif, il y'a également une erreur et le mobre de munition dimunu de 1"""

class MyTestCase(unittest.TestCase):
    def test_fire_at_anti_air(self):
        b = wp.Lance_missiles_antiair()
        try:
            b.fire_at(2, 3, -1)
        except wp.Range_Munition as exc:

            print("erreur, message :", exc)

        except wp.NoAmmunitionError as exc:
            print("erreur, message :", exc)

        except wp.OutOfRangeError as exc:
            print("erreur, message :", exc)

            print(b)  # normalement on doit avoir 49 munitions car le z est négatif

            self.assertEqual(50, b.ammunition)


if __name__ == '__main__':
    unittest.main()
