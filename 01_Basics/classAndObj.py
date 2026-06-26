class Employee:
    """
    As we know that class is blueprint so here 
    A class to represent a company employee blueprint.
    """

    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id         
        self.emp_name = name          
        self.dept = department        
        self.salary = salary  
        
        #  The right-side parameter (like 'name') is a temporary local variable
        # accessible ONLY inside this constructor function. like below print()
        # But variables attached to 'self' (like 'self.emp_name') become instance attributes,
        # making them accessible ANYWHERE inside this class (and even outside via the object)!
        print("name of employee", name, "has been added")

    def get_details(self):
        # Using self.emp_name here works because it's bound to the object instance!
        return f'ID {self.emp_id} , NAME :{self.emp_name} has Department :{self.dept}'

    def get_salary(self):
        return f'salary of {self.emp_name} is {self.salary}'


# CREATING OBJECT INSTANCES
emp1 = Employee(101, "Alice Smith", "Engineering", 8000)
emp2 = Employee(emp_id=102, name="Bob Jones", department="Design", salary=6500)
emp3 = Employee(103, "Inayat Shah", "Cybersecurity", 9200)
emp4 = Employee(104, "ahmad noore", "Cybersecurity", 9000) # Removed "$" to keep it a pure integer

# EXECUTING METHODS 
print("\n--- Execution Output ---")
print(emp1.get_details())  
print(emp2.get_salary())  
print(emp3.get_salary())   
print(emp4.get_salary())