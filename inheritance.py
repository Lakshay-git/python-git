class A:
    def __init__(self):
        print("init of class A")
    
    def method1(self):
        print("this is method 1")

    def method2(self):
        print("this is method 2")

class B(A):
    def __init__(self):
        print("init of class B")
    
    def method3(self):
        print("this is method 3")
    
    def method4(self):
        print("this is method 4")

class C(B):
    def __init__(self):
        super().__init__()
        print("init of class C")
    def method5(self):
        print("this is method 5")

obj=C()
 
