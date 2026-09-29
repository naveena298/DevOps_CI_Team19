import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from cab_booking import calculate_fare, get_cab_details


def test_calculate_fare():
    assert calculate_fare(10, 15) == 150


def test_cab_details():
    assert get_cab_details("Mini") == 12
    assert get_cab_details("Sedan") == 15
    assert get_cab_details("SUV") == 20