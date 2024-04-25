import my_functions
import json
from datetime import datetime


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def save(self, file_path):
        with open(file_path, 'w') as file:      # 'w' bedeutet, dass die Datei zum Schreiben geöffnet wird
            json.dump(self.__dict__, file)


class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name) #super() ruft __init__ von Elternklasse also Person auf


class Subject(Person):
    def __init__(self, first_name, last_name, sex, date_of_birth):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__date_of_birth__ = date_of_birth
        self.age = self.age_from_birthdate()
        self.est_max_hr = self.estimate_max_hr()
        
    def age_from_birthdate(self):
        today = datetime.now()
        birth_date = datetime.strptime(self.__date_of_birth__, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
    def estimate_max_hr(self):
        estimate_max_hr = my_functions.estimate_max_hr(self.age, self.sex)
        return estimate_max_hr



class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self, file_path):
        with open(file_path, 'w') as file:      # 'w' bedeutet, dass die Datei zum Schreiben geöffnet wird
            json.dump(self.__dict__, file)
