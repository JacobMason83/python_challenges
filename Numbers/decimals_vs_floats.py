#importing decimal
from decimal import Decimal
# in python there is a decimal library and a nice introduction to import an outside library
product_cost = 88.40
commision_rate = 0.08
qty = 450

# product_cost += (commision_rate * product_cost)
# print(product_cost * qty) #float value = 42962.4

product_cost = Decimal(88.40)
commision_rate = Decimal(0.08)
qty = 450

product_cost += (commision_rate * product_cost)

print(product_cost * qty) #42962.40000000000282883716451 is the decimal number and this is better used in scientific calculations like with nasa who used floating point and caused a crash


