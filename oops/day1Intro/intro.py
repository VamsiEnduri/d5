# # what is oops ? why we need oops ? in a pr lang?
# # import math
# # print(math)
# # ooops is object oriented pr lang which helps us to maintain modular pr parts , each part :-- data, functions class

# # class a:
# #     name="vamsi"
# #     def abc():
# #         print(name)

# # class b:
# #     name="ravi"
# #     age=27
# #     def abc():
# #         print(name,age)



# class Vamsi:
#     #varibles
#     name="vamsi"
#     age=27

#     # default constructor method
#     def __init__():
#         #code

#     # functions
#     def details():
#         print(name,age)
class linkedInPost:
    def __init__(self,img,msg):
        self.image=img
        self.message=msg
        print(type(self),"self type")

    def postDetails(self):
        print("hlo",self.image,self.message) 
a=linkedInPost("../../../../Desktop/ReactWorkFlowProject.png","today day 1 of 100 days python learning challenge")
a.postDetails()