class Ashok:
    def __init__(self,name,work):
        self.name = name
        self.work = work
    def details1(self):
        print(f"My father's name is {self.name} and he works in {self.work}")
    
class ishan(Ashok):
    def __init__(self,name,work,name1,work1):
        Ashok.__init__(self,name,work)
        self.name1 = name1
        self.work1 = work1
    def details(self):
        print(f"My name is {self.name1} and I study in {self.work1}")        
obj = ishan("Ashok","JLT","Ishan","IIS")
obj.details()
obj.details1()