from Source import add_student_data
from Source import remove_student_data
from Source import search_student_data
from unittest import TestCase


class Testing(TestCase):
    def test_get_roll_number(self):
        exp = isinstance(add_student_data.get_roll_list(), list)
        self.assertTrue(expr=exp)

    def test_add_student_data(self):
        # Testing by adding new data
        self.assertTrue(add_student_data.add_student("59732", "John", "9874354233"))

        # Testing by adding invalid phone number
        self.assertFalse(add_student_data.add_student("59732", "John", "98743543"))

        # Testing by adding student that is already in the file
        self.assertFalse(add_student_data.add_student("79478937", "John", "9874354233"))

    def test_search_student(self):
        # Testing by adding valid roll number
        self.assertTrue(search_student_data.search_student("79478937"))

        # Testing by adding invalid roll number
        self.assertFalse(search_student_data.search_student("1567"))

    def test_remove_student(self):
        # Testing by adding valid roll number
        self.assertTrue(remove_student_data.remove_student("647328"))

        # Testing by adding invalid roll number
        self.assertFalse(remove_student_data.remove_student("1567"))
