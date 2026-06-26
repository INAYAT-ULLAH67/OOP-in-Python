class Developer:
    def execute_code(self):
        return "Running code optimization algorithms."

class Robot:
    def execute_code(self):
        return "Executing logic routines based on processor instructions."

# A uniform function that doesn't care about the object's class type
def start_operation(worker_object):
    print(worker_object.execute_code())

# Testing completely unrelated classes
dev = Developer()
bot = Robot()

start_operation(dev) 
start_operation(bot)  