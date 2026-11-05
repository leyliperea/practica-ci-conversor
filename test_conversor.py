from conversor import *

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(100) == 212

def test_fahrenheit_a_celsius():
    assert fahrenheit_a_celsius(212) == 100

def test_celsius_a_kelvin():
    assert celsius_a_kelvin(0) == 273.15
