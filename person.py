class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class employee(person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
class customer(person):
    def __init__(self,name,age,customer_id):
        super().__init__(name,age)
        self.customer_id=customer_id
person = person("john doe",30)
employee = employee("jane smith",25,"E21")
customer = customer("varghese",18,"C14")
print(person.name,person.age)
print(employee.name,employee.age,employee.employee_id)
print(customer.name,customer.age,customer.customer_id)