class Employee:
    count=0
    def __init__(self,Name,Id,sal):    #self reprenets the current object.
        self.Name=Name
        self.Id=Id
        self.sal=sal
        Employee.count+=1
    def disp(self):
        print('Name=',self.Name,'Id=',self.Id,'salary=',self.sal)
E1=Employee("Sujit",101,7000)
E2=Employee("sayan",102,80000)
E1.disp()
E2.disp()
print(Employee.count)
