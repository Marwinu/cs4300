import pytest
import numpy as np
from src.task7 import calculate_mean, calculate_max, calculate_sum

numbers = np.array([10, 20, 30, 40, 50])

def test_mean():
    assert calculate_mean(numbers) == 30.0

def test_max():
    assert calculate_max(numbers) == 50

def test_sum():
    assert calculate_sum(numbers) == 150