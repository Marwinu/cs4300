import pytest
from src.task4 import calculate_discount

def test_discount_int():
    # int price, int discount
    assert calculate_discount(50, 10) == 45
    assert calculate_discount(50, 50) == 25
    assert calculate_discount(50, 100) == 0
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(100, 50) == 50
    assert calculate_discount(100, 100) == 0
    assert calculate_discount(200, 10) == 180
    assert calculate_discount(200, 50) == 100
    assert calculate_discount(200, 100) == 0

def test_discount_float():
    # float price, float discount
    assert calculate_discount(10.50, 10.0) == pytest.approx(9.45)
    assert calculate_discount(10.50, 50.0) == pytest.approx(5.25)
    assert calculate_discount(10.50, 100.0) == pytest.approx(0.0)
    assert calculate_discount(100.0, 10.0) == pytest.approx(90.0)
    assert calculate_discount(100.0, 50.0) == pytest.approx(50.0)
    assert calculate_discount(100.0, 100.0) == pytest.approx(0.0)

def test_discount_mixed():
    # int price, float discount
    assert calculate_discount(50, 10.5) == pytest.approx(44.75)
    assert calculate_discount(100, 50.5) == pytest.approx(49.5)
    assert calculate_discount(200, 99.5) == pytest.approx(1.0)
    # float price, int discount
    assert calculate_discount(10.50, 10) == pytest.approx(9.45)
    assert calculate_discount(100.0, 50) == pytest.approx(50.0)
    assert calculate_discount(200.0, 100) == pytest.approx(0.0)

# Input validation
def test_invalid_inputs():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)   # invalid price
    with pytest.raises(TypeError):
        calculate_discount(100, "10")   # invalid discount
    with pytest.raises(TypeError):
        calculate_discount("100", "10") # both invalids

    # None type cases
    with pytest.raises(TypeError):
        calculate_discount(None, 10)    # No price
    with pytest.raises(TypeError):
        calculate_discount(100, None)   # no discount
    with pytest.raises(TypeError):
        calculate_discount(None, None)  # nothing