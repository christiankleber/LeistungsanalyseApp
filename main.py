import my_functions
import json

experiment_name = input("Enter the name of the experiment: ")
date = input("Enter the date of the experiment: ")
supervisor = input("Enter the first name of the supervisor: ")
subject = input("Enter the subject of the experiment: ")

experiment = my_functions.build_experiment(experiment_name, date, supervisor, subject) 
print(experiment)

with open("sample.json", "w") as outfile: 
    json.dump(experiment, outfile)