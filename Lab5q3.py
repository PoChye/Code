#Student ID: 1201201352
#Student Name: Tan Po Chye

def main():
    print("======================================")
    print("                 MENU                 ")            
    print("======================================") 
    print("1.    Convert centimeter to meter")
    print("2.    Convert meter to centimeter")        
    print("======================================")
    choice = int(input("Enter your choice : "))
    if(choice == 1):
        get_cm()
    elif(choice == 2):
        get_m()
    else:
        print("Invalid choice!")

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter: "))
    m = cm_to_meter(cm)
    print(" {:.2f} cm is {:.2f} meter ".format(cm, m))

def m_to_cm(meter):
    centimeter = meter * 100
    return centimeter

def get_m():
    m = float(input("Please enter a value for meter: "))
    cm = m_to_cm(m)
    print(" {:.2f} meter is {:.2f} cm ".format(m , cm))
    
main()
