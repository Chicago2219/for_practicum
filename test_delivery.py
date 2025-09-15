import pytest
from delivery import calculate_delivery, LoadLevel

def test_minimum_cost():
    assert calculate_delivery(1, is_big=False, fragile=False, load=LoadLevel.LOW) == 400

def test_distance_rules():
    assert calculate_delivery(1, False, False, LoadLevel.LOW) == 400
    assert calculate_delivery(5, False, False, LoadLevel.LOW) == 400
    assert calculate_delivery(15, False, False, LoadLevel.LOW) == 400
    assert calculate_delivery(35, False, False, LoadLevel.LOW) > 400

def test_big_vs_small():
    small = calculate_delivery(35, is_big=False, fragile=False, load=LoadLevel.LOW)
    big = calculate_delivery(35, is_big=True, fragile=False, load=LoadLevel.LOW)
    assert big > small

def test_fragile_within_limit():
    cost = calculate_delivery(5, is_big=False, fragile=True, load=LoadLevel.LOW)
    assert cost > 400

def test_fragile_over_limit():
    with pytest.raises(ValueError):
        calculate_delivery(50, is_big=False, fragile=True, load=LoadLevel.LOW)

def test_load_multipliers():
    base = calculate_delivery(35, is_big=True, fragile=False, load=LoadLevel.LOW)
    very_high = calculate_delivery(35, is_big=True, fragile=False, load=LoadLevel.VERY_HIGH)
    assert very_high > base
