# class HariKrishna:
#     surName="nandamuri" # parent class varible
#     def __init__(self,n,a,cp):# parent args
#         self.nameP=n # parent instance varibles
#         self.ageP=a
#         self.currentProjectP=cp 
#         print(self.surName,self.nameP,self.ageP,self.currentProjectP,"7th line parent class line")

#     def details(self):
#         print("nandamuri family")


# class NTR(HariKrishna):
#     prof="actor"
#     def __init__(self,n,a,cp,pn,pa,pcP): # params child ntr
#         self.name=n # child instance varaibles
#         self.age=a
#         self.currentProject=cp 
#         super().__init__(pn,pa,pcP) #args # calling parent method
#         print(super().surName,self.name,self.age,self.currentProject,"19th line child class line")
#         super().details()
#     def movies(self):
#         print("total 30 movies as of now")    

# obj=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # obj2=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # obj3=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # obj=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # obj=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # obj=NTR("jr.ntr",42,"NTRNEEL","hkrishna","expired","sitayya") # args ntr args
# # print(obj.prof,"24th line")
# # obj.movies()
# # HariKrishna.details(10)
class Employee_10000Coders:
    companyName="10000coders"
    def __init__(self,rm1,rm2):
        self.reportMang1=rm1 
        self.reportMang2=rm2

class Sr_Tariner(Employee_10000Coders):
    def __init__(self,n,a,s,rm1="akhil",rm2="rakesh"): #parms
        self.name=n 
        self.age=a 
        self.sepc=s 
        super().__init__(rm1,rm2) # args

    def emp_details(self):
        print(f"{self.name} is with age of {self.age} with spec {self.sepc} and wprking in {super().companyName} to reporting for {self.reportMang1,self.reportMang2}")    

class jr_Trainer(Sr_Tariner):
    def __init__(self):
        pass     
emp1=Sr_Tariner("vamsi",27,"DS&PYTHON&MERN","akhil","rakesh")
emp2=Sr_Tariner("chaitanya",32,"DS&PYTHON&MERN","rakesh")
emp1.emp_details()
emp2.emp_details()