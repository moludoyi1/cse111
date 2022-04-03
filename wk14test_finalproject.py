import pytest
import random
from wk14finalproject import get_hours_test, get_hourly_pay_rate_test,\
    calculate_weekly_pay, get_weekly_income, get_dict_key_test, \
    get_state_income_tax_rate, get_state_income_tax_dict, get_bills

def test_get_hours():
    assert isinstance(get_hours_test(20.5), float)


def test_get_hourly_pay_rate():
    assert isinstance(get_hourly_pay_rate_test(11.50), float)

def test_calculate_weekly_pay():
    csvlist = [0.0200, 0.0495, 0.0307]
    
    for i in range(10):
        index = random.randint(0, len(csvlist)-1)
        tax_rate = csvlist[index]
        weekly_pay =  random.randint(0, 2000)

        assert calculate_weekly_pay(weekly_pay, tax_rate) >= 0


def test_get_weekly_income():
    """"Check if it is return the right calculations
        Parameters: 2 
        Retrun: int"""
        
    assert get_weekly_income(5, 10) == 50

# def test_get_dict_key_():
    
    # assert isinstance(get_dict_key_test("Florida", str))

def test_get_state_income_tax_rate():
    state_dict = get_state_income_tax_dict("csvData.csv")
    state_dict_value = list(state_dict.values())
    state_dict_keys = list(state_dict.keys())
    count = 0
    for i in state_dict_keys:
        assert get_state_income_tax_rate(state_dict, i) == float(state_dict_value[count][1])
        count +=1
    
def test_get_state_income_tax_dict():
    for i in range(10):
        assert len(get_state_income_tax_dict("csvData.csv")) > 0

# def test_get_bills():
#     # bills_list = [["spotify", "insurance", "car insurance"], [4.99, 99, 49]]
#     for i in range(2):
#         assert len(get_bills()) > 0

pytest.main(["-v", "--tb=line", "-rN", __file__])