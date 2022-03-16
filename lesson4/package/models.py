

# Class Person for creat person
# Class Person have ready methods - (info, change_salary)


class Person:

    def __init__(self, username, salary):
        self.username = username
        self.salary = salary

    #     Info method for get Person information
    #  return str() in terminal


    def info(self):
        print(f'Username: {self.username}\nSalary: {self.salary} ')

    #  change salary method for change attribute salary in
    #  class Person, after change salary,  return call self.info()

    def change_salary(self, new_salary):
        self.salary = new_salary
        self.info()