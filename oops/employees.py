class Employee:
    # class level variable
    employees = []

    # initializing instance variables
    def __init__(self, name, email, position) -> None:
        self.name = name
        self.email = email
        self.position = position

    # function to add employee
    def add_employee(self):
        employee = [self.name, self.email, self.position]
        Employee.employees.append(employee)
        print("Employee Added Successfully.")

    @classmethod
    def display_info(cls):
        print("-----------------------------------------------------------")
        print("Displaying User Informations")
        print("-----------------------------------------------------------")
        for datas in cls.employees:
            print("Name : ", datas[0])
            print("Email : ", datas[1])
            print("Position: ", datas[2])
            print("-----------------------------------------------------------")


emp1 = Employee("Pujan", "pujan@gmail.com", "Developer")
emp2 = Employee("John", "john@gmail.com", "Manager")
emp3 = Employee("Mary", "mary@hotmail.com", "Designer")

emp1.add_employee()
emp2.add_employee()
emp3.add_employee()

Employee.display_info()
