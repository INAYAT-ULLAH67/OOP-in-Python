class Student:
    def __init__(self, name, roll_no):
        self.name = name
        
        # 1. Internal Storage: Hidden behind a single underscore (Protected)
        self._roll_no = roll_no  

    # ==========================================
    # 2. THE GETTER
    # ==========================================
    @property
    def roll_no(self):
        """Acts as a read-only gateway when accessing 'student.roll_no'"""
        print("[Getter] Intercepted read request. Fetching roll number safely...")
        return self._roll_no

    # ==========================================
    # 3. THE SETTER
    # ==========================================
    @roll_no.setter
    def roll_no(self, new_roll):
        """Acts as a security guard when executing 'student.roll_no = value'"""
        print(f"[Setter] Intercepted write request. Validating value: {new_roll}")
        
        # Data Validation Rules
        if not isinstance(new_roll, int):
            print("❌ Type Error: Roll number must be a pure integer!")
        elif new_roll <= 0:
            print("❌ Value Error: Roll number must be a positive integer!")
        else:
            print("✅ Validation Passed: Memory updated successfully.")
            self._roll_no = new_roll


# ==========================================
# EXECUTING AND TESTING THE PROPERTY
# ==========================================

# Instantiating the object
s1 = Student("Inayat", 67)

print("\n--- Step 1: Reading Data via Getter ---")
# Accesses the method WITHOUT parentheses (), treating it like a normal variable
print(f"Student Roll No: {s1.roll_no}")  

print("\n--- Step 2: Attempting an Invalid String Update ---")
# The setter catches the bad data type and blocks it
s1.roll_no = "Sixty-Seven"  

print("\n--- Step 3: Attempting an Invalid Negative Update ---")
# The setter catches the mathematical error and blocks it
s1.roll_no = -5

print("\n--- Step 4: Performing a Valid Update ---")
# The setter approves this integer and updates self._roll_no
s1.roll_no = 88

print("\n--- Step 5: Verifying the Final State ---")
print(f"Updated Roll No: {s1.roll_no}")