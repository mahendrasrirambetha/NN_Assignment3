'''
Neural Network Deep Learning
ICP 3
author: Mahendra Sriram Betha
student ID: 700757819


In class programming:
1. Create a class Employee and then do the following
• Create a data member to count the number of Employees
• Create a constructor to initialize name, family, salary, department
• Create a function to average salary
• Create a Fulltime Employee class and it should inherit the properties of Employee class
• Create the instances of Fulltime Employee class and Employee class and call their member functions.
'''

# Created Employee class with name, family, salary and department
class Employee:

    # declared a data member to count the number of Employees
    no_of_employees = 0

    # constructor to initialize the object's attributes
    def __init__(self, name, family_name, salary, department):
        self.__name = name
        self.__family_name = family_name
        self.salary = salary
        self.__department = department
        Employee.no_of_employees += 1

    # declared average_salary function to return average salary 
    def average_salary(employees):
        """
        function to average salary
        """
        sum = 0
        for employee in employees:
            sum += employee.salary
        return sum / Employee.no_of_employees

# Created a Fulltime Employee class and inherited the properties of Employee class
class FulltimeEmployee(Employee):
    """
    Full Time Employee is a sub class of Employee
    """

    def __init__(self, name, family_name, salary, department):
        super().__init__(name, family_name, salary, department)

    def full_time_member(self):
        print("Calling FulltimeEmployee member function.")

# Created the instances of Fulltime Employee class and Employee class and calling their member functions.
def main():
    employees = []
    full_time_employee1 = FulltimeEmployee("Mahi", "Betha", 123000, "Software Engineering")
    full_time_employee1.full_time_member()
    employees.append(full_time_employee1)
    full_time_employee2 = FulltimeEmployee("Sangeetha", "Baddam", 134500, "Cyber Security")
    employees.append(full_time_employee2)
    employee1 = Employee("Bhavani", "Miryala", 1670000, "Testing")
    employees.append(employee1)
    employee2 = Employee("Rakesh", "Reddy", 192000, "Product Manager")
    employees.append(employee2)
    print("Average salary:", FulltimeEmployee.average_salary(employees))

# declared this method to execute code When the file runs as a script.
if __name__ == "__main__":
    main()


2. Numpy
Using NumPy create random vector of size 20 having only float in the range 1-20.
Then reshape the array to 4 by 5
Then replace the max in each row by 0 (axis=1)
(you can NOT implement it via for loop)
'''
import numpy as nump

# created a random vector of size 20 with float values between 1 and 20
randomvec = nump.random.uniform(low=1, high=20, size=20)
print(randomvec)
# reshape the array to 4 by 5 using reshape method
mat45 = randomvec.reshape(4, 5)
print(mat45)
# replace the max in each row by 0 using where method
mat45 = nump.where(mat45 == nump.amax(mat45, axis=1, keepdims=True), 0, mat45)
print(mat45)
