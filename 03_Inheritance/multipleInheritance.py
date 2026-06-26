class A:
    def show(self):
        print("A works")

class B:
    def show(self):
        print("B works")
       
class C(B,A):
    # pass
    def show(self):
        print("C works")

objC=C()
objC.show()
# Way 1: Check it via the Class name directly (Recommended)
print(C.__mro__)  
