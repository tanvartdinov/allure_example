# python -m unittest tests/test_main.py


import unittest
from unittest import TestCase
from main import factorial, summarize
from phonebook import PhoneBook


class TestMain(TestCase):
    def test_summarize_1(self):
        # Правило AAA
        # Arrange
        x = 5
        y = 7
        expected = 12

        # Act
        result = summarize(x, y)

        # Assert
        self.assertEqual(expected, result)

    @unittest.expectedFailure
    def test_summarize_2(self):
        x = 0
        y = 7
        expected = 7

        result = summarize(x, y)

        self.assertEqual(expected, result)

    @unittest.skipIf(True, 'Боевой сервер')
    def test_summarize_3(self):
        x = 0
        y = 7
        expected = 7

        result = summarize(x, y)

        self.assertEqual(expected, result)

    def test_summarize_4(self):
        x = 5
        y = -7
        expected = -2

        result = summarize(x, y)

        self.assertEqual(expected, result)

    def test_with_params(self):
        for i, (a, b, expected) in enumerate((
                (5, 7, 12),
                (5, -7, -2),
                (-5, 7, 2)
        )):
            with self.subTest(i):
                result = summarize(a, b)
                self.assertEqual(expected, result)

    def test_raises(self):
        self.assertRaises(ValueError, summarize, 1, 6)


class TestPhoneBook(TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()
        self.phonebook.add_contact('Мама', 124124124)
        self.phonebook.add_contact('папа', 999999999)
        self.phonebook.add_contact('братан', 345345623)
        self.phonebook.add_contact('Васек', 457373434)
        self.phonebook.add_contact('ПАПА', 888888888)

    def tearDown(self):
        del self.phonebook

    def test_create_empty_book(self):
        phonebook = PhoneBook()
        self.assertEqual(len(phonebook.get_all_contacts()), 0)

    def test_add_contact(self):
        self.assertEqual(len(self.phonebook.get_all_contacts()), 4)

    def test_find_contact_success(self):
        self.assertEqual(self.phonebook.find_contact('Папа'), 888888888)

    def test_find_contact_failed(self):
        self.assertIsNone(self.phonebook.find_contact('Жора'))


class TestFactorial(TestCase):
    def test_negative_number(self):
        self.assertRaises(ValueError, factorial, -4)

    def test_non_integer_number(self):
        self.assertRaises(ValueError, factorial, 4.5)

    def test_positive(self):
        self.assertEqual(factorial(6), 720)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)
