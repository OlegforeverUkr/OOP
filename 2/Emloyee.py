class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return 'I come to the office.'

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary


class Recruiter(Employee):
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} SALARY - {self.salary}'

    def work(self):
        return 'I come to the office and start to hiring.'


class Developer(Employee):
    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} SALARY - {self.salary}'

    def work(self):
        return 'I come to the office and start to coding.'


roma = Recruiter('Roma', 1000)
vasya = Developer('Vasya', 1500)
print(f'{roma}\n{vasya}')
print(roma == vasya)
print(vasya > roma)
