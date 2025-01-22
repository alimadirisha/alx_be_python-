import unittest
from simple_calculator import simple_calculator.py

class TestSimpleCalculator(unittest.TestCase)

def setUp(self):
        
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)  
        self.assertEqual(self.calc.add(-1, 1), 0)  
        self.assertEqual(self.calc.add(0, 0), 0) 
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)  

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6) 
        self.assertEqual(self.calc.multiply(0, 5), 0)  
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)  

    def test_division(self):
        self.assertEqual(self.calc.divide(6, 3), 2)  
        self.assertEqual(self.calc.divide(-6, 3), -2) 
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)  
        with self.assertRaises(ZeroDivisionError):  # Test division by zero
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()