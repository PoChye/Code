#Student ID: 1201201352
#Student Name: Tan Po Chye

def rectangle(width, length):
    area = width * length
    return area

def triangle(width, length):
    area = 0.5 * width * length
    return area

width = float(input("Enter width  : "))
length = float(input("Enter length : "))
recarea = rectangle(width, length)
triarea = triangle(width, length)
print("Rectangle area : {:.2f} ".format(recarea))
print("Triangle are : {:.2f}".format(triarea))