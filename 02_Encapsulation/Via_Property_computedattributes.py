class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """Dynamically calculates the full name on the fly"""
        return f"{self.first_name} {self.last_name}"

u = User("Inayat", "Shah")
print(u.full_name)  # Output: Inayat Shah