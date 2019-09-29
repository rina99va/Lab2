import unittest
import lab1

class Test_TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertTrue(lab1.Calculator.Add(self))
    def test_divide(self):
        self.assertTrue(lab1.Calculator.Divide(self))
    def test_modulo(self):
        self.assertEqual(lab1.Calculator.Modulo(self), 0)

if __name__ == '__main__':
    unittest.main()
