# if the sale price is 3.21 then it should be 3.99 or 3.00 
# pretty_price(3.20, 0.99) 
# pretty_price(3.20, 0.99)
import math
from math import *



def pretty_price(num1, num2):
    num1 = math.floor(num1)
    num2 = float(num2)
    if type(num1) == float or type(num2) == float:
        return num1 + (num2/100)
    
    elif  type(num1) != float or type(num1) != int:
        return f'You didnt enter a valid input please try again '
    
    elif  type(num2) != float or type(num2) != int:
        return f'You didnt enter a valid input please try again '

    
print(pretty_price(3.20, 99))
print(pretty_price(1.23, 99))
print(pretty_price(3.20, 55))
print(pretty_price(3.20, 55))


# jordans solution 
def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 25))



