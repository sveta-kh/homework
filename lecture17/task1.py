#Employee → Manager

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
    @salary.deleter
    def salary(self):
        del self.__salary        


class Manager(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        print(self.name, self.department, self.salary)

manager1 = Manager("Ana", 5000, "IT")
manager1.get_info()

manager1.salary = 8000
manager1.get_info()

manager1.salary = -3000
manager1.get_info()

del manager1.salary

