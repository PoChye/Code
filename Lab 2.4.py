
#Student ID: 1201201352
#Student Name: Tan Po Chye

bns=1.50
grp=5.60

print("Invoice for Fruits Purchase")
print("---------------------------------")
qtybns = float(input("Enter the quantity (comb) of bananas bought: "))
qtygrp = float(input("Enter the amount (kg) of grapes bought: "))

ttlbns = qtybns * bns
ttlgrp = qtygrp * grp
ttlprc = ttlbns + ttlgrp
print("Item             Qty         Price          Total")
print("Banana (combs)   {}          RM{:.2f}       RM{:.2f}".format(qtybns,bns,ttlbns))
print("Grapes (kg)      {}          RM{:.2f}       RM{:.2f}".format(qtygrp, grp,ttlgrp))

print("Total RM{:.2f} ".format(ttlprc))