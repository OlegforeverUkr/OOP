from unittest import TestCase
from Cadidates import Candidate


class TestOne(TestCase):
    def setUp(self) -> None:
        self.candidates_test = [{'first_name': 'Ivan', 'last_name': 'Chechov', 'email': 'ichech@example.com',
                                 'tech_stack': 'Python|Django|Angular', 'main_skill': 'Python',
                                 'main_skill_grade': ' Senior'},
                                {'first_name': 'Max', 'last_name': 'Payne', 'email': 'mpayne@example.com',
                                 'tech_stack': 'PHP|Laravel|MySQL', 'main_skill': 'PHP', 'main_skill_grade': 'Middle'},
                                {'first_name': 'Tom', 'last_name': 'Hanks', 'email': 'thanks@example.com',
                                 'tech_stack': 'Python|CSS', 'main_skill': 'Python', 'main_skill_grade': 'Junior'}]
        self.one_candidate = Candidate(first_name="Ivan",
                                       last_name='Korzh',
                                       email='thanks@example.com',
                                       tech_stack='Python|CSS',
                                       main_skill='Python',
                                       main_skill_grade='Middle')
        self.candidates_test_http = Candidate.generate_candidates(
            'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
        self.candidates_test_csv = Candidate.generate_candidates('candidates.csv')

    def test_fullname(self):
        self.assertEqual(self.one_candidate.full_name, 'Ivan Korzh')

    def test_generate_http(self):
        self.assertEqual(len(self.candidates_test_http), len(self.candidates_test))
        self.assertIsInstance(self.candidates_test_http[0], Candidate)
        self.assertNotEqual(self.candidates_test_http[0].email, 'example@example.com')
        self.assertNotEqual(self.candidates_test_http[1].email, 'example@example.com')
        self.assertEqual(self.candidates_test_http[2].email, 'thanks@example.com')

    def test_generate_csv(self):
        self.assertEqual(len(self.candidates_test_csv), len(self.candidates_test))
        self.assertIsInstance(self.candidates_test_http[0], Candidate)
        self.assertNotEqual(self.candidates_test_http[0].email, 'example@example.com')
        self.assertNotEqual(self.candidates_test_http[1].email, 'example@example.com')
        self.assertEqual(self.candidates_test_http[2].email, 'thanks@example.com')