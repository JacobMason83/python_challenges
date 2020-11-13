from decimal import Decimal
product_cost = 88.40
commision_rate = 0.08
qty = 450

print(int(product_cost)) # returns 88
print(float(qty))# returns 450.0
print(Decimal(product_cost))  #88.400000000000005684341886080801486968994140625
print(complex(commision_rate)) # returns (0.08+0j) which is scientific notation 