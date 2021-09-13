#Student ID:1201201352
#Student Name:Tan Po Chye

alw=0.15

print("Natural Mineral Water Dispenser")
print("---------------------------------")

qtyalw = float(input("Enter amount of litres: "))
total = qtyalw * alw
print("Price per litre  = RM 0.15")
print("Number of liters = {}".format(qtyalw))
print("Total RM {:.2f} ".format(total))