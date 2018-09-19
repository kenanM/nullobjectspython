from unittest import TestCase

from number_null_objects_example import product, sum
from optional import optional_of_nullable, optional_of, empty


class NumbersNullObjectsTest(TestCase):
    def test_null_product_example(self):
        assert product(optional_of(5), empty()) == 0

    def test_product_actually_works_with_some_numbers(self):
        assert product(optional_of(5), optional_of(5)) == 25

    def test_null_sum_example(self):
        assert sum(empty(), optional_of(5)) == 5

    def test_sum_actually_works_with_some_numbers(self):
        assert sum(optional_of(5), optional_of(5)) == 10
