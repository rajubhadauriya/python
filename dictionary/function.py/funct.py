"""syntax:
def function_name():
    print()/return"""
# def anyprint():
#     print("hello function")

# anyprint()
# def r():
#     for r in range(1,31):
#         print(r,end=" ")

# r()
d1={}

def emp_add():
    id=int(input("enter employee id"))
    name=input("enter employee name")
    salary=int(input("enter employee salary"))
    d1[id]=[name,salary]
def emp_update():
    id=int(input("enter employee id u want update"))
    if id in d1:
        new_name=input("enter new name")
        new_salary=int(input("enter new salary"))
        d1[id][0]=new_name
        d1[id][1]=new_salary
    else:
        print("no such employee exist")
def emp_del():
    id=int(input("enter employee id you want delete:"))
    if id in d1:
        del d1[id]
    else:
        print("no such employee exist")
def emp_disply():
    print(d1)
def main():
    while True:
        print("1.add employee")
        print("2.delete employee")
        print("3.update employee")
        print("4.search employee")
        print("5.display employee")
        print("6.exit employee")
        choice=int(input("enter ur choice : "))
        if choice==1:
            emp_add()
        elif choice==2:
            emp_del()
        elif choice==3:
            emp_update()
        elif choice==4:
            emp_search()
        elif choice==5:
            emp_disply()
        elif choice==6:
            break
        else:
            print("enter correct choice")
main()        
print(d1)


        
