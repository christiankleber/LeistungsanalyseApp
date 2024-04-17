import my_functions
import json


class Person():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        estimate_max_hr = my_functions.estimate_max_hr(self.age, self.sex)
        return estimate_max_hr
    
    def __dict__(self):
        return {"first_name": self.first_name, 
                "last_name": self.last_name, 
                "age": self.age, 
                "estimate_max_hr": self.estimate_max_hr()}
    
    def save(self, file_path):
        with open(file_path, 'w') as file:      # 'w' bedeutet, dass die Datei zum Schreiben geöffnet wird
            json.dump(self.__dict__(), file)




class Experiment():
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject