
from fizzbuzz.fizzbuzz import fizzbuzz


def test_given_1_return_1():
    assert fizzbuzz(1) == "1"


def test_given_2_return_2():
    assert fizzbuzz(2) == "2"

    
def test_given_3_return_Fizz():
    assert fizzbuzz(3) == "Fizz"

    
def test_given_6_return_Fizz():
    assert fizzbuzz(6) == "Fizz"


def test_given_5_return_Buzz():
    assert fizzbuzz(5) == "Buzz"

    
def test_given_10_return_Buzz():
    assert fizzbuzz(10) == "Buzz"

    
def test_given_15_return_FizzBuzz():
    assert fizzbuzz(15) == "FizzBuzz"

    
def test_given_15_return_FizzBuzz():
    assert fizzbuzz(30) == "FizzBuzz"
