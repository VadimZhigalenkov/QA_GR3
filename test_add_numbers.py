import pytest

def add_numbers(*args):
    return sum(args)

@pytest.fixture(params=[(2,3),(5,-2,10),(0,0,5,-5)])
def numbers_for_test(request):
    return request.param

def test_add_numbers(numbers_for_test):
    result = add_numbers(*numbers_for_test)
    expected = sum(numbers_for_test)
    assert result == expected