from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("John", "Smith") == "Smith; John"
    assert make_full_name("Brandon", "Alder") == "Alder; Brandon"
    assert make_full_name("Joseph", "Smith") == "Smith; Joseph"

def test_extract_family_name():
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("Alder; Brandon") == "Alder"
    assert extract_family_name("Smith; Joseph") == "Smith"

def test_extract_given_name():
    assert extract_given_name("Smith; John") == "John"
    assert extract_given_name("Alder; Brandon") == "Brandon"
    assert extract_given_name("Smith; Joseph") == "Joseph"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])