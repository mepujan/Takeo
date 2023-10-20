class Company:
    def __init__(self, name, location, revenue, profit) -> None:
        self.name = name
        self.location = location
        self.__revenue = revenue
        self.__profit = profit

    def company_info(self):
        # print("Company Name : ", self.name)
        # print("Company Location: ", self.location)
        print("Company Revenue: ", self.__revenue)
        print("Company Profit: ", self.__profit)


class Employee(Company):
    def __init__(self, emp_name, emp_location, salary, bank_account_number, name, location, revenue, profit) -> None:
        self.emp_name = emp_name
        self.emp_location = emp_location
        self.__salary = salary
        self.__bank_account_number = bank_account_number
        super().__init__(name, location, revenue, profit)

    def employee_info(self):
        print("Employee Name: ", self.emp_name)
        print("Employee Location: ", self.emp_location)
        print("Employee Salary: ", self.__salary)
        print("Company Name: ", self.name)
        print("Company Location: ", self.location)


employee1 = Employee("Pujan", "Mississauga", '30000',
                     '123456', 'Takeo Inc', 'New York', 100000, 5000000)
employee1.employee_info()
employee1.company_info()
