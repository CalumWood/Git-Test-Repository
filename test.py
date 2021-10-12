import unittest
import app

class TestMethods(unittest.TestCase):
    def test_squared(self):
        squareNumbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        for i in range(1, 10):
            self.assertEqual(app.squared(i), squareNumbers[i-1])

    def test_cubed(self):
        self.assertEqual(app.cubed(3), 27)
    
    def test_squareRoot(self):
        self.assertEqual(app.squareRoot(9), 3)

if __name__ == '__main__':
    unittest.main()