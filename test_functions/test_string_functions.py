import unittest
from more_functions import string_functions as multi


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual("AyahAyahAyah", multi.multiply_string("Ayah", 3))


if __name__ == '__main__':
    unittest.main()
