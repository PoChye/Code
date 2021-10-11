#Student ID: 1201201352
#Student Name: Tan Po Chye

def my_function(name, contact_no, age, salary, overtime):
    print("Hello this is my name: ", name)
    print("This is my phone number: ", contact_no)
    print("This is my age: ", age)
    total=float(salary)+float(overtime)
    print("Your salary this month is :", total)

my_function("Tan Po Chye", "0123456789", "19", 3000, 300)