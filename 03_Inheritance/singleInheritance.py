# ==========================================
# 1. THE PARENT CLASS (Superclass)
# ==========================================
class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.emp_name = name
        self.dept = department
        self.salary = salary  # Base salary

    def get_details(self):
        """Generic method to fetch baseline employee credentials."""
        return f"ID: {self.emp_id} | Name: {self.emp_name} | Dept: {self.dept}"

    def calculate_payout(self):
        """Returns total compensation."""
        return self.salary


# ==========================================
# 2. THE CHILD CLASS (Subclass)
# ==========================================
# Manager inherits EVERYTHING from Employee
class Manager(Employee):
    def __init__(self, emp_id, name, department, salary, team_size, bonus):
        # Pass the core attributes up to the Employee parent constructor
        super().__init__(emp_id, name, department, salary)
        
        # Add attributes unique ONLY to a Manager
        self.team_size = team_size
        self.bonus = bonus

    # METHOD OVERRIDING: A manager's payout calculation includes their bonus!
    def calculate_payout(self):
        """Overrides parent method to include managerial bonus."""
        return self.salary + self.bonus

    def manage_team(self):
        """A specialized method that only managers can execute."""
        return f"Manager {self.emp_name} is currently supervising a team of {self.team_size} engineers."
    
# 1. Creating a standard Employee instance
regular_emp = Employee(101, "Alice Smith", "Engineering", 8000)

# 2. Creating a Manager instance (The Child)
mgr = Manager(202, "Inayat Shah", "Cybersecurity", 12000, team_size=8, bonus=2500)


print("--- 1. Testing Regular Employee ---")
print(regular_emp.get_details())       # Output: ID: 101 | Name: Alice Smith | Dept: Engineering
print(f"Payout: {regular_emp.calculate_payout()}") # Output: Payout: 8000
# print(regular_emp.manage_team())     # ❌ CRASHES! Regular employees cannot manage_team().


print("\n--- 2. Testing Manager (Single Inheritance) ---")
# Calling an INHERITED method (Defined in Employee, used perfectly by Manager)
print(mgr.get_details())               # Output: ID: 202 | Name: Inayat Shah | Dept: Cybersecurity

# Calling a UNIQUE child method
print(mgr.manage_team())               # Output: Manager Inayat Shah is currently supervising a team of 8 engineers.

# Calling the OVERRIDDEN method (Python runs the Manager version, not the Employee version)
print(f"Total Manager Payout: {mgr.calculate_payout()}") 
# Output: Total Manager Payout: 14500 (12000 base + 2500 bonus)