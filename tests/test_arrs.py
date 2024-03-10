import unittest
from utils.arrs import get, my_slice

class TestFunctions(unittest.TestCase):

    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(get(array, 2), 3)

    def test_get_non_existing_index(self):
        array = [1, 2, 3, 4, 5]
        self.assertIsNone(get(array, 10))

    def test_get_with_default(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(get(array, 10, default="Not found"), "Not found")

    def test_my_slice_normal(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, 1, 4), [2, 3, 4])

    def test_my_slice_empty_collection(self):
        coll = []
        self.assertEqual(my_slice(coll, 0, 2), [])

    def test_my_slice_negative_start(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, -3), [3, 4, 5])

    def test_my_slice_negative_end(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, end=-2), [1, 2, 3])

    def test_my_slice_empty_list(self):
        coll = []
        self.assertEqual(my_slice(coll), [])

    def test_my_slice_negative_start_and_end(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, -3, -1), [3, 4])

    def test_my_slice_negative_start_and_end_reverse(self):
        coll = [1, 2, 3, 4, 5]
        self.assertEqual(my_slice(coll, -1, -3), [])

