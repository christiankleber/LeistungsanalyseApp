import my_classes

experiment_name = input("Enter the name of the experiment: ")
date = input("Enter the date of the experiment: ")
supervisor = input("Enter the first name of the supervisor: ")
subject = input("Enter the subject of the experiment: ")

experiment = my_classes.Experiment(experiment_name, date, supervisor, subject) 
experiment.save("experiment.json")

first_name = input("Enter the first name of the supervisor: ")
last_name = input("Enter the last name of the supervisor: ")
sex = input("Enter sex of the supervisor: ")
age = int(input("Enter age of the supervisor: "))

supervisor = my_classes.Supervisor(first_name, last_name, sex, age)
supervisor.save("supervisor.json")

first_name = input("Enter the first name of the subject: ")
last_name = input("Enter the last name of the subject: ")
sex = input("Enter sex of the subject: ")
age = int(input("Enter age of the subject: "))
birthdate = input("Enter birthdate of the subject: ")

subject = my_classes.Subject(first_name, last_name, sex, age, birthdate)
subject.save("subject.json")