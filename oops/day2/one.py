# # oops :
# obj ori we build our software in way of modular progarmming
# and with the helps of oops 

# modular progarmming
# reuse
# security
# scalability

# # <module "in-built">
# # <class 'int'>

# oops :-- 
# class  :-- it is palce where all my feature varibles and featire functions will be palced
# class :-- it is abp for real world object r real world feature
# class a: #contains attributes (varaibles) and properties (functions)

# class a:
#     x=10
#     y=20
#     z=30
#     def __init__(self):
#         pass
#     def abc(self):
#         pass
#     def xyz(self):
#         pass  
# # object :--
# vamsi=a()
# print(vamsi)
name="vamsi"
age=27
batch="d5"
edu="it"
class addStudent:
    def __init__(self,n,a,b,e):
        self.stu_name=n
        self.stu_age=a
        self.stu_batch=b 
        self.stu_edu=e
    def detailsStu(self):
        print(self.stu_age)
            
stuObj=addStudent(name,age,batch,edu)    
print(stuObj.stu_name,"45") 
stuObj.detailsStu() 



name="vamsi"
age=27
batch="d5"
edu="it"
class addStudent:
    batchName="D5"
    totalStu=35
    def __init__(self):
        pass
        # self.stu_name=name
        # self.stu_age=age
        # self.stu_batch=batch 
        # self.stu_edu=edu
    def detailsStu(a):
        print(a.age)
        print(a.name)
    detailsStu(10)    
            
stuObj=addStudent()    
# print(stuObj.stu_name,"45") 
stuObj.detailsStu()
stuObj.__init__()