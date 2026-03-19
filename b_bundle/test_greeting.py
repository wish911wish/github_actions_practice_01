import unittest
from greeting import greet, farewell


class TestGreeting(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")

    def test_farewell(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")
        self.assertEqual(farewell("Bob"), "Goodbye, Bob!")

    def test_greet_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_farewell_empty_name(self):
        with self.assertRaises(ValueError):
            farewell("")


if __name__ == "__main__":
    unittest.main()
