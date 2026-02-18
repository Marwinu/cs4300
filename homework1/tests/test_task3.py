
import pytest
from src.task3 import define_state, first_prime_nums, sum_nums

def test_define_state():
    assert define_state(20) == "positive"
    assert define_state(-5) == "negative"
    assert define_state(0) == "zero"

def test_first_prime_nums():
    confirmed_prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert first_prime_nums(0) == []
    assert first_prime_nums(1) == [2]
    assert first_prime_nums(15) == confirmed_prime_nums

def test_sum_nums():
    assert sum_nums(1) == 1
    assert sum_nums(100) == 5050
    assert sum_nums(50) == 1275
    assert sum_nums(0) == 0
    assert sum_nums(3) == 6