from unittest import TestCase
from Emloyee import Employee, Developer, Recruiter
import datetime


class TestOne(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.empploye = Employee(name="Boris",
                                 salary=2000,
                                 )

    def test_salary(self):
        self.assertEqual(self.empploye.check_salary(10), 14000)

    def test_work(self):
        self.assertIsInstance(self.empploye.work(), str)


class TestTwo(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.recrut = Recruiter(name="Andrey",
                                salary=1700,
                                )

    def test_work(self):
        self.assertEqual(self.recrut.work(), 'I come to the office and start to hiring.')

    def test_different_salary(self):
        self.assertEqual(self.recrut.check_salary(2), 3400)


class TestThree(TestCase):
    def setUp(self) -> None:
        self.data = datetime.date.today()
        self.dev = Developer(name="Jora",
                             salary=1500,
                             tech_stack=['java', 'C#'],

                             )

    def test_work(self):
        self.assertEqual(self.dev.work(), 'I come to the office and start to coding.')
