from unittest import TestCase
from unittest import mock
from unittest.mock import patch
from emloyee import Employee, Developer, Recruiter, Logger
import datetime


class TestEmployee(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.employee = Employee(name="Boris",
                                 salary=2000,
                                 )

    def test_salary(self, mock_method):
        self.assertEqual(self.employee.check_salary(10), 14000)

    def test_work(self):
        self.assertIsInstance(self.employee.work(), str)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='borya@mail.com')
    def test_open_file(self, mock_file):
        expected_result = 'borya@mail.com'

        with open('emails.csv') as file:
            result = file.read()

        self.assertEqual(expected_result, result)

    @patch('tests.TestEmployee.test_open_file', return_value='borya@mail.com')
    def test_error_mail(self, test_open_file):
        expected_result = 'vasya@mail.com'
        self.assertNotEqual(test_open_file(), expected_result)


class TestRecruiter(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.recrut = Recruiter(name="Andrey",
                                salary=1700,
                                )

    def test_work(self):
        self.assertEqual(self.recrut.work(), 'I come to the office and start to hiring.')

    def test_different_salary(self):
        self.assertEqual(self.recrut.check_salary(2), 3400)


class TestDeveloper(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.dev1 = Developer(name="Jora",
                             salary=1500,
                             tech_stack=['java', 'C#'],
                             )
        self.dev2 = Developer(name="Vova",
                              salary=1500,
                              tech_stack=['java', 'C#', 'Python'],
                              )

    def test_work(self):
        self.assertEqual(self.dev1.work(), 'I come to the office and start to coding.')

    def test_eq(self):
        self.assertEqual(self.dev1 == self.dev2, False)
        self.assertNotEqual(self.dev1 != self.dev2, False)
        self.assertEqual(self.dev1 < self.dev2, True)

    def test_lt(self):
        self.assertEqual(self.dev1 == self.dev2, False)
        self.assertNotEqual(self.dev1 != self.dev2, False)
        self.assertEqual(self.dev1 > self.dev2, False)

    def test_salary(self):
        self.assertEqual(self.dev1.check_salary(10), self.dev2.check_salary(10))
        self.assertNotEqual(self.dev1.check_salary(10) < self.dev2.check_salary(10), True)

    def test_error(self):
        with self.assertRaises(Exception):
            self.dev1 < TestEmployee
            self.dev1 == TestEmployee
            self.dev1 != TestEmployee
            self.dev1 > TestEmployee
            self.dev2 < TestEmployee
            self.dev2 == TestEmployee
            self.dev2 != TestEmployee
            self.dev1 > TestEmployee
