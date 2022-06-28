import pytest
from app.calculator import Calculator

class TestCalc:
    def setup (self):
        self.calc = Calculator


    def test_multiply_calculate_correctly (self):        #тестирование операции "умножение"
        assert self.calc.multiply(self, 3, 6) == 18

    def test_division_calculate_correctly (self):        #тестирование операции "деление"
        assert self.calc.division(self, 10, 5) == 2

    def test_subtraction_calculate_correctly (self):       #тестирование операции "вычитание"
        assert self.calc.subtraction(self, 20, 15) == 5

    def test_adding_calculate_correctly (self):           #тестирование операции "сложение"
        assert self.calc.adding(self, 13, 12) == 25

