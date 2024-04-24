import my_functions
import json


class Person():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

class Supervisor(Person):
    pass

class Subject(Person):
    def __init__(self, first_name, last_name, sex, age, birthdate):
        super().__init__(first_name, last_name, sex, age)
        self.__birthdate = birthdate
        self.est_max_hr = self.estimate_max_hr()
     
    def estimate_max_hr(self):
        estimate_max_hr = my_functions.estimate_max_hr(self.age, self.sex)
        return estimate_max_hr

class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, filename):
        with open(filename, 'w') as file:    
            json.dump(self.__dict__, file)

if __name__ == "__main__":
    subject = Subject("John", "Doe", "male", 25, "1995-01-01")
    file = subject.save("subject.json")