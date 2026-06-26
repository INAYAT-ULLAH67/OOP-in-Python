from abc import ABC, abstractmethod

# ==========================================
# 1. THE ABSTRACT BLUEPRINT
# ==========================================
class MobilePhone(ABC):
    
    @abstractmethod
    def turn_on_flashlight(self):
        """Every phone class must override this method."""
        pass


# ==========================================
# 2. CONCRETE CHILD CLASSES
# ==========================================
class iPhone(MobilePhone):
    def turn_on_flashlight(self):
        return "iPhone: Sending signal to Apple hardware API -> LED Flash active! 🔦"


class AndroidPhone(MobilePhone):
    def turn_on_flashlight(self):
        return "Android: Invoking Camera2 hardware Manager -> LED Flash active! 🔦"


# ==========================================
# 3. EXECUTING THE BLUEPRINT
# ==========================================

# ❌ This line would CRASH because you cannot instantiate MobilePhone directly:
# my_phone = MobilePhone()

# Creating actual phone objects
devices = [iPhone(), AndroidPhone()]

for phone in devices:
    print(phone.turn_on_flashlight())