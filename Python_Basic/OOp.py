class Student:#class==blueprint
    def __init__(self, name):#self==instance of the class(must have include self keyword )
        self.name = name# enter name
        

    def introduce(self):#method
        return f" I am {self.name} "  
student1 = Student("John")#object creats
print(student1.introduce())