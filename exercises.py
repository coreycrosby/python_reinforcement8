#Exercise 1

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

    def __repr__(self):
        return f"{self.description}: {self.due_date}"


#Exercise 2

class TodoList:
    def __init__(self, name):
        self.name = name
        self.to_do_list = []
    
    def add_task(self, task):
        self.to_do_list.append(task)
        

practice_coding = Task("Practice Coding", "Tonight")
dinner_date = Task("Dinner Date", "Tomorrow night")
commute_home = Task("Commute Home", "After class")

my_list = TodoList("My list")

print(my_list.to_do_list)
my_list.add_task(practice_coding)

print(my_list.to_do_list)
my_list.add_task(dinner_date)

print(my_list.to_do_list)
my_list.add_task(commute_home)

print(my_list.to_do_list)
