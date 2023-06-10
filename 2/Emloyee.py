import csv
from Exception import EmailAlreadyExistsException

TODAY = 28
HOLIDAYS = 6


class Employee:
    def __init__(self, name, salary, email=''):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()

    def work(self):
        return 'I come to the office.'

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def check_salary(self, days, holiday=0):
        if not holiday:
            return self.salary * days
        else:
            minus_salary = self.salary * holiday
            return self.salary * days - minus_salary

    def save_email(self):
        with open('emails.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.email])

    def validate(self):
        with open('emails.csv', 'r') as file:
            text = csv.reader(file)
            for i in text:
                if i == self.email:
                    raise EmailAlreadyExistsException


class Recruiter(Employee):
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} SALARY - {self.salary}'

    def work(self):
        return 'I come to the office and start to hiring.'


class Developer(Employee):

    def __init__(self, *args, tech_stack, **kwargs):
        super().__init__(*args, **kwargs)
        self.tech_stack = tech_stack

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} SALARY - {self.salary}, STACK - {self.tech_stack}, \'' \
               f'email - {self.email}'

    def work(self):
        return 'I come to the office and start to coding.'

    def __eq__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) == len(other.tech_stack)
        return 'Invalid data'

    def __lt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) < len(other.tech_stack)
        return 'Invalid data'

    def __gt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) > len(other.tech_stack)
        return 'Invalid data'

    def __add__(self, other):
        name = f'{self.name} {other.name}'
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.salary, other.salary)
        return Developer(name, salary, tech_stack=tech_stack, email=f'{self.email} {other.email}')


roma = Recruiter('Roma', 1000, email='recrut@roma.com')
vasya = Developer('Vasya', 1500, tech_stack=['java', 'python', 'C++'], email='dev@vasya.com')
vanya = Developer('Roma', 1700, tech_stack=['java', 'C#'], email='num@vanya.com')
print(roma == vasya)
print(vasya > roma)
print(roma.check_salary(TODAY, HOLIDAYS))
# petya = vasya + vanya
# print(petya)
# print(vasya > vanya)
# print(vasya == vanya)
