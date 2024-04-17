import my_functions
import json
import my_classes


# Hier werden die Attribute für das Experiment abgefragt
experiment_name = input("Enter the name of the experiment:   ")
date = input("Enter the date of the experiment: ")
supervisor = input("Enter the first name of the supervisor: ")
subject = input("Enter the subject of the experiment: ")

experiment = my_classes.Experiment(experiment_name, date, supervisor, subject)
experiment.save("experiment.json")

# Hier werden die Attribute für den Supervisor abgefragt
first_name = input("Enter the first name of the supervisor: ")
last_name = input("Enter the last name: ")
sex = input("Enter sex: ")
age = input("Enter age: ")

supervisor = my_classes.Person(first_name, last_name, sex, age)
supervisor.save("supervisor.json")

# Hier werden die Attribute für den Subject abgefragt
first_name = input("Enter the first name of the subject: ")
last_name = input("Enter the last name: ")
sex = input("Enter sex: ")
age = input("Enter age: ")

subject = my_classes.Person(first_name, last_name, sex, age)
subject.save("subject.json")
