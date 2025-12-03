#  multiple and heirarchial inheritance 
# ambiguity isues 
class parent1:
    surName="endurip1"
    p1Name="srinu"
    def ap1(self):
        print("ap1 method")

class parent2:
    surName="endurip2"
    p2Name="anjali"
    def ap2(self):
        print("ap2 method")
    
class child(parent2,parent1):
    def __init__(self,n,a,l):
        self.name=n
        self.age =a 
        self.loc= l 
        # print(super().p1Name)
        # print(super().p2Name)
        # print(parent1.surName)#endurip1
        # print(parent2.surName)#endurip2
        # super().ap1()
        # super().ap2()

    def childDetails(self):
        print(f"{self.name} is with age of {self.age} and living in {self.loc} location with surname {parent1.surName}") 
    # childDetails()

class child2(parent1,parent2):
    def __init__(self,n,a,l):
        self.name=n
        self.age =a 
        self.loc= l 
    def childDetails2(self):
        print(f"{self.name} is with age of {self.age} and living in {self.loc} location with surname {parent1.surName}")
        parent1.ap1(10) 

abc=child("srilekha",29,"gujarat")
abc2=child2("vamsi",27,"hyd")
abc.childDetails()
abc2.childDetails2()

