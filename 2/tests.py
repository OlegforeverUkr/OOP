from unittest import TestCase
from unittest import mock
from Emloyee import Employee, Developer, Recruiter
import datetime


class TestEmployee(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.empploye = Employee(name="Boris",
                                 salary=2000,
                                 )

    def test_salary(self):
        self.assertEqual(self.empploye.check_salary(10), 14000)

    def test_work(self):
        self.assertIsInstance(self.empploye.work(), str)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='borya@mail.com')
    def test_open_file(self, mock_file):
        expected_result = 'borya@mail.com'

        with open('emails.csv') as file:
            result = file.read()

        self.assertEqual(expected_result, result)

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='borya@mail.com')
    def test_error_mail(self, mock_file):
        expected_result = 'vasya@mail.com'

        with open('emails.csv') as file:
            result = file.read()

        self.assertNotEqual(result, expected_result)


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
        self.dev = Developer(name="Jora",
                             salary=1500,
                             tech_stack=['java', 'C#'],
                             )

    def test_work(self):
        self.assertEqual(self.dev.work(), 'I come to the office and start to coding.')
