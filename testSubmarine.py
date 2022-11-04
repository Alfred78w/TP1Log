import unittest
import Vessel as vs
import Weapon as wp

class MyTestCase(unittest.TestCase):
    def test_go_to_submarine(self):
        a=vs.Submarine((2,2,1))
        try:
            a.go_to(50, 50, -1)
        except vs.CoordinateError as exc:
            print('erreur, message:', exc)
        #except vs.DestroyedError as exc:
            #print('erreur, message:', exc)
        #except wp.OutOfRangeError as exc:
           # print('erreur, message:', exc)

        self.assertEqual((2,2,1), a.coordinates)  # add assertion here


if __name__ == '__main__':
    unittest.main()
