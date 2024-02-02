import collections
import unittest
import random
import string
import re
import app
from collections import *
from app import *


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, count_common_elements([1, 2, 3], [4, 5, 6]))
        self.assertEqual(1, count_common_elements([1, 2], [1, 3]))
        self.assertEqual(3, count_common_elements([1, 2, 3], [1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
