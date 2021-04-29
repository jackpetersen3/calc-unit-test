import unittest
import calc

class testCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5,9), 14)
        self.assertEqual(calc.add(1,2), 4)
    def test_sub(self):
        self.assertEqual(calc.sub(10,5), 5)
        self.assertEqual(calc.sub(2,1), 3)
    def test_mult(self):
        self.assertEqual(calc.mult(3,3), 9)
        self.assertEqual(calc.mult(1,1), 2)
    def test_div(self):
        self.assertEqual(calc.div(6,2), 3)
        self.assertEqual(calc.div(6,2), 7)

if __name__ == "__main__":
    unittest.main()