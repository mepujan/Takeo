class Employee:
    def __init__(self, employee_id, name, level) -> None:
        self.employee_id = employee_id
        self.name = name
        self.level = level

    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, employee_id, name, level) -> None:
        super().__init__(employee_id, name, level)

    def calculate_salary(self):
        return 100000 if self.level == "senior" else 800000


class Developer(Employee):
    def __init__(self, employee_id, name, level) -> None:
        super().__init__(employee_id, name, level)

    def calculate_salary(self):
        return 80000 if self.level == "senior" else 50000


class Designer(Employee):
    def __init__(self, employee_id, name, level) -> None:
        super().__init__(employee_id, name, level)

    def calculate_salary(self):
        return 60000 if self.level == "senior" else 45000


manager1 = Manager("102", "Jack", "senior")
manager2 = Manager("103", "Tom", "junior")

print("Salary of employee id ", manager1.employee_id,
      " is : $", manager1.calculate_salary())
print("Salary of employee id ", manager2.employee_id,
      " is : $", manager2.calculate_salary())

developer1 = Developer("901", "Pujan", "junior")
developer2 = Developer("902", "Ram", "senior")

print("Salary of employee id ", developer1.employee_id,
      " is : $", developer1.calculate_salary())
print("Salary of employee id ", developer2.employee_id,
      " is : $", developer2.calculate_salary())


designer1 = Designer("501", "Anil", "senior")
designer2 = Designer("502", "Aseem", "junior")

print("Salary of employee id ", designer1.employee_id,
      " is : $", designer1.calculate_salary())
print("Salary of employee id ", designer2.employee_id,
      " is : $", designer2.calculate_salary())
