from db_connection import db_connection_func
a=db_connection_func()
curObj=a.cursor() # you need to have it



def add_student():
    s_adNo=int(input("enetr student id here :---- "))
    s_name=input("enter student name here :-- ")
    s_age=int(input("enter student age here :--- "))
    s_year=int(input("enter which year stidents is"))
    s_dept=input("enter student dept here ")
    
    # query="insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values (%s,%s,%s,%s,%s)"
    curObj.execute("insert into students (stu_admNo,stu_name,stu_age,stu_year,stu_dept) values (%s,%s,%s,%s,%s)",(s_adNo,s_name,s_age,s_year,s_dept)) # it will execute yr sql query
    # insert, update, delte from python to db :-- commit()
    a.commit()
    print("addedd succesfuly to db")