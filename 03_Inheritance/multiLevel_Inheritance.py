# ==========================================
# 1. THE GRANDPARENT CLASS
# ==========================================
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.emp_name = name

    def basic_info(self):
        return f"ID: {self.emp_id} | Name: {self.emp_name}"


# ==========================================
# 2. THE PARENT CLASS (Inherits from Employee)
# ==========================================
class Manager(Employee):
    def __init__(self, emp_id, name, department):
        # super() looks up one level and calls Employee.__init__
        super().__init__(emp_id, name)
        self.department = department

    def manager_info(self):
        return f"Department: {self.department}"


# ==========================================
# 3. THE CHILD CLASS (Inherits from Manager)
# ==========================================
class Director(Manager):
    def __init__(self, emp_id, name, department, stock_options):
        # super() looks up one level and calls Manager.__init__
        # Manager.__init__ will then call Employee.__init__ automatically!
        super().__init__(emp_id, name, department)
        self.stock_options = stock_options

    def director_info(self):
        return f"Stock Options: {self.stock_options} shares"
    

# Creating a Director instance (at the bottom of the chain)
director_obj = Director(
    emp_id=5001, 
    name="Inayat Shah", 
    department="Cybersecurity", 
    stock_options=1500
)

print("--- Testing Multilevel Inheritance Data Access ---")

# 1. Accessing a Grandparent method
print(director_obj.basic_info())      
# Output: ID: 5001 | Name: Inayat Shah

# 2. Accessing a Parent method
print(director_obj.manager_info())    
# Output: Department: Cybersecurity

# 3. Accessing its own Child method
print(director_obj.director_info())   
# Output: Stock Options: 1500 shares