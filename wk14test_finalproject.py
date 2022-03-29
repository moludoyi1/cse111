
from wk14finalproject import get_weekly_income, calculate_weekly_pay
import pytest

def test_get_weekly_income():
    """"Check if it is return the right calculations
        Parameters: none
        Retrun: weekly income"""
        
    assert get_weekly_income(5, 10) == 50


pytest.main(["-v", "--tb=line", "-rN", __file__])