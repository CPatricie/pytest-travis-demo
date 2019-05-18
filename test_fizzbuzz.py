from fizzbuzz import fizzbuzz
import pytest

def test_fb_is_callable_with_1_argument():
	fizzbuzz(1)


def test_fb_returns_str():
	assert isinstance(fizzbuzz(1), str) # zadám věc, třída, zjistí pokud je věc instancí té třídy

@pytest.mark.parametrize("num", [1, 2, 4])
def test_fb_regular_is_self(num):
# def test_fb_is_1():
	assert int(fizzbuzz(num)) == num


@pytest.mark.parametrize("num", [3, 6, 9])
def test_fb_three_is_fizz(num):
	assert fizzbuzz(num) == "fizz"


@pytest.mark.parametrize("num", [5, 20, 50])
def test_fb_three_is_buzz(num):
	assert fizzbuzz(num) == "buzz"


@pytest.mark.parametrize("num", [15, 30, 3000])
def test_fb_three_is_fizzbuzz(num):
	assert fizzbuzz(num) == "fizzbuzz"


@pytest.mark.parametrize("num", ["", 1.5, [], 4+3j])
def test_fb_raises_typeerror_on_nonint(num):
	with pytest.raises(TypeError):
		fizzbuzz(num)

"""
@pytest.mark.parametrize("num", ["", -1, -30])
def test_fb_raises_typeerror_on_nonpositive(num):
	with pytest.raises(TypeError):
		fizzbuzz(num)
"""		