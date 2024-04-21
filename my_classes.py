import my_functions
import json


class Person():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.est_max_hr = self.estimate_max_hr()
     
    def estimate_max_hr(self):
        estimate_max_hr = my_functions.estimate_max_hr(self.age, self.sex)
        return estimate_max_hr


    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)


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
    person = Person("John", "Doe", "male", 25)
    max_hr = person.estimate_max_hr()
    file = person.save("person.json")
    print(max_hr)