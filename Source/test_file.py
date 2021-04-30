from Source import main
from Source import add_student_data
from Source import remove_student_data
from Source import search_student_data
from unittest import TestCase


def test_get_roll_number():
    exp = isinstance(add_student_data.get_roll_list(), list)
    print(exp)
    #TestCase.assertTrue(exp)


print(test_get_roll_number())
