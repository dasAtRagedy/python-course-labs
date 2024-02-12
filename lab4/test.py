import unittest
from fibonaccimodule import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_base_case(self) -> None:
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_negative_input(self) -> None:
        with self.assertRaises(IndexError):
            fibonacci(-1)
        with self.assertRaises(IndexError):
            fibonacci(-5)
    
    def test_non_integer_input(self) -> None:
        with self.assertRaises(TypeError):
            fibonacci("a")
        with self.assertRaises(TypeError):
            fibonacci("0")

if __name__ == "__main__":
    unittest.main()