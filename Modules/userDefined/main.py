from register import reg
from login import log

while True:
    print("choose below ..")
    print("1.register")
    print("2.login")
    
    op=input("enter yr option here :--- ")
    if op == "1":
        reg()
    if op == "2":
        log()    