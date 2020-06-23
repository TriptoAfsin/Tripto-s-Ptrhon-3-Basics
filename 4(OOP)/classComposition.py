class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return(self.pay*12)+self.bonus


class Employee: #Employee is the container 
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus) #Salary class is the content 

    def total_salary(self):
        return self.obj_salary.annual_salary() 


employee1 = Employee("Tripto", 22, 25000, 10000)

print(employee1.total_salary())

       