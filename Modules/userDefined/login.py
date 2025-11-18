from register import rUsers
from dashboard import dashboard___
# currentLoginUserEmail=None
# a=10
def log():
    e=input("enter email here :--  ")
    p=input("enetr password here :-- ")
    for ruser in rUsers:
        if e==ruser["email"] and p ==ruser["pswd"]:
            print("successfully logedin")
            # global currentLoginUserEmail
            # currentLoginUserEmail=e
            dashboard___(e)
