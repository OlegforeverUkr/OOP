import requests
import csv


class Candidate:
    __CANDIDATES = []

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 tech_stack,
                 main_skill,
                 main_skill_grade,
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def generate_candidates(cls, file):

        if file.startswith('http'):
            return cls.get_candidates(file)

        else:
            with open(file, 'r') as file:  # Create a class object from file
                read = csv.reader(file)
                print(read)
                next(read)
                for x in read:
                    characters = x[0]
                    all_name = [x for x in characters.split(';')]
                    all_name.pop()
                    first_name, last_name = all_name[0].split()
                    email = all_name[1]
                    tech_stack = all_name[2]
                    main_skill = all_name[3]
                    main_skill_grade = all_name[4]
                    candidate = cls(first_name,
                                    last_name,
                                    email,
                                    tech_stack,
                                    main_skill,
                                    main_skill_grade)
                    cls.__CANDIDATES.append(candidate)

            return cls.__CANDIDATES

    @classmethod
    def get_candidates(cls, http):
        request = requests.get(http)
        text = request.text
        lines = text.split('\n')
        lines.pop()

        for i in lines[1:]:
            characters = i.split(',')
            all_name = [x for x in characters[0].split()]
            first_name = all_name[0]
            last_name = all_name[1]
            characters.pop(0)
            characters.insert(0, first_name)
            characters.insert(1, last_name)
            new_candidate = cls(*characters)
            cls.__CANDIDATES.append(new_candidate)

        return cls.__CANDIDATES

    def __str__(self):
        return f'{self.first_name}, ' \
               f'{self.last_name}, ' \
               f'{self.email}, ' \
               f'{self.main_skill_grade}'


ivan = Candidate('Ivan',
                 'Morozov',
                 'email@vas.com',
                 'PHP|Laravel|MySQL',
                 'PHP',
                 'Middle',
                 )

for i in Candidate.get_candidates(
        'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'):
    print(i.__dict__)
