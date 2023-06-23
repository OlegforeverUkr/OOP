import csv
import datetime
from exception import EmailAlreadyExistsException

TODAY = datetime.date.today()


class Logger:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result is True:
                self.write_log()
            return result

        return wrapper

    @staticmethod
    def write_log():
        time = datetime.datetime.now()
        error = f"{time} | {EmailAlreadyExistsException('Error: This email already exist')}\n"
        with open('logs.txt', 'a') as file1:
            file1.write(error)
        raise EmailAlreadyExistsException('Error: This email already exist')


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

    def check_salary(self, days):
        today = datetime.date.today()
        working_days = 0
        for i in range(1, days + 1):
            all_days = datetime.date(today.year, today.month, i)
            if all_days.weekday() < 5:
                working_days += 1
        return working_days * self.salary

    def save_email(self):
        with open('emails.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.email])

    @staticmethod
    def write_log():
        time = datetime.datetime.now()
        error = f"{time} | {EmailAlreadyExistsException('Error: This email already exist')}\n"
        with open('logs.txt', 'a') as file1:
            file1.write(error)

    @Logger()
    def validate(self):
        with open('emails.csv', 'r') as file:
            read_file = csv.reader(file)
            for i in read_file:
                if self.email in i:
                    return True


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
        raise Exception('Different classes for comparison')

    def __lt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) < len(other.tech_stack)
        raise Exception('Different classes for comparison')

    def __gt__(self, other):
        if isinstance(other, Developer):
            return len(self.tech_stack) > len(other.tech_stack)
        raise Exception('Different classes for comparison')

    def __add__(self, other):
        name = f'{self.name} {other.name}'
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.salary, other.salary)
        return Developer(name, salary, tech_stack=tech_stack, email=f'{self.email} {other.email}')


if __name__ == "__main__":
    roma = Recruiter('Roma', 1200, email='recrut@roma.com')
    vasya = Developer('Vasya', 1500, tech_stack=['java', 'python', 'C++'], email='dev@vasya.com')
    vanya = Developer('Vanya', 1700, tech_stack=['java', 'C#'], email='num@vanya.com')
    print(roma == vasya)
    print(vasya > roma)
    print(roma.check_salary(TODAY.day))
    petya = vasya + vanya
    print(petya)
    print(vasya > vanya)
    print(vasya == vanya)
    print(roma)

