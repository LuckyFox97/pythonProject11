import unittest
from utils.arrs import get, my_slice

class TestFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(get(array, 2), 3)

    def test_get_non_existing_index(self):
        array = [1, 2, 3]
        self.assertEqual(get(array, 5, 'default'), 'default')

    def test_my_slice_full_range(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll), coll)

    def test_my_slice_with_start(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, 1), [2, 3, 4, 5])

    def test_my_slice_with_end(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, end=3), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()