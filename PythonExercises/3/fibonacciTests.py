import unittest
import doctest
import fibo
import fibonacciTestsDoc

class FibonacciTests(unittest.TestCase):
    def test_value_0(self):
        with self.assertRaises(ValueError):
            fibo.fibonacciNumberAtPosition(0)

    def test_value_05(self):
        with self.assertRaises(ValueError):
            fibo.fibonacciNumberAtPosition(0.5)

    def test_value_string(self):
        with self.assertRaises(ValueError):
            fibo.fibonacciNumberAtPosition("string")

    def test_value_1(self):
        self.assertEqual(fibo.fibonacciNumberAtPosition(1), 0)

    def test_value_2_and_3(self):
        self.assertIs(fibo.fibonacciNumberAtPosition(2), fibo.fibonacciNumberAtPosition(3))

    def test_value_10(self):
        self.assertNotEqual(fibo.fibonacciNumberAtPosition(10), 10)

testSuite = unittest.TestSuite()
testSuite.addTests(unittest.makeSuite(FibonacciTests))

testSuite.addTest(doctest.DocTestSuite(fibonacciTestsDoc))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(testSuite)
