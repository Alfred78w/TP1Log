import unittest
import Weapon as wp


class MyTestCase(unittest.TestCase):
    def test_fire_at_antisurface(self):
        # lance_missile_antisurface
        a = wp.Lance_missiles_antisurface()
        try:
            a.fire_at(2, 3, 1)
        except wp.Range_Munition as exc:

            print("erreur, message :", exc)

        except wp.NoAmmunitionError as exc:
            print("erreur, message :", exc)

        except wp.OutOfRangeError as exc:
            print("erreur, message :", exc)

        print(a) # normalement on doit avoir 39 munitions car le z different de 0

        self.assertEqual(39, a.ammunition)


if __name__ == '__main__':
    unittest.main()
