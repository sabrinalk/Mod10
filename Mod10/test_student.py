"""
Program: test_student.py
Author: Sabrina Khothisen
Last date modified: 11/16/2023
Purpose: test a class using unit tests
"""

import unittest
from Mod10.class_definitions.student_class import Student as stu


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = stu("Kho", "Sab", "Math")

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, "Kho")
        self.assertEqual(self.student.first_name, "Sab")
        self.assertEqual(self.student.major, "Math")

    def test_object_created_all_attributes(self):
        student = stu("Kho", "Sab", "Math", 3.4)
        assert student.last_name == "Kho"
        assert student.first_name == "Sab"
        assert student.major == "Math"
        assert student.gpa == 3.4

    def test_student_str(self):
        self.assertEqual(str(self.student), "Kho, Sab has major Math with gpa: 0.0")

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            s = stu("123", "Sab", "Math")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            s = stu("Kho", "123", "Math")

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            s = stu("Kho", "Sab", "123")

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            s = stu("Kho", "Sab", "Math", "three")


if __name__ == '__main__':
    unittest.main()