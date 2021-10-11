#Student ID: 1201201352
#Student Name: Tan Po Chye

def get_bonus(unit, salary):
    if(unit>1000):
        bnsamt = salary * 0.2
    elif(unit>501 and unit<1000):
        bnsamt = salary * 0.1
    else:
        bnsamt = 0
    return bnsamt

def get_nett_salary(salary, bnsamt):
    nettsalary = bnsamt + salary
    return nettsalary

def display(staffid, salary, unit, bnsamt, nettsalary): 
    print("\nStaff ID                : ", staffid)
    print("Staff salary            :  RM {:.2f}".format(salary))
    print("Units sold              : ", unit)
    print("Bonus                   :  RM {:.2f}".format(bnsamt))
    print("Nett Salary             :  RM {:.2f}".format(nettsalary))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                DATA ENTRY                  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
staffid = int(input("Enter staff id          : "))
salary = float(input("Enter staff salary      : RM "))
unit = int(input("Enter total units sold  : "))

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("               SALARY SLIP                  ")           
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
bnsamt = get_bonus(unit, salary)
nettsalary = get_nett_salary(salary, bnsamt)
display(staffid, salary, unit, bnsamt, nettsalary)