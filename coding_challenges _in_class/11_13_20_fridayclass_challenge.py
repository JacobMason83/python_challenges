# import functools
# from functools import reduce



# def manual_exponent (base, power):
#     base = 1
#     collection = [base] *power
#     return reduce(lambda (total,element: total * element ,collection)



# print(manual_exponent(10, 2))
# print(manual_exponent(2, 3))
# print(manual_exponent(1, 3))
# print(manual_exponent(2, 3))
# print(manual_exponent(2, 3))

from functools import reduce, total_ordering

# manual way 
# def manual_exponent(num, exp):
#     counter = exp - 1
#     total = num
    
#     while counter > 0:
#         total *= num 
#         counter -= 1
#     return total 


# print(manual_exponent(2, 3))
# print(manual_exponent(2, 3))
# print(manual_exponent(2, 3))
# print(manual_exponent(2, 3))

def manual_exponent (num, exp)
    computed_list = [num] * exp
    return (reduce(lambda total, element:total * element, computed_list))


    # return reduce (lambda a, b:Pedmas , list) # easier way to look at reduce function  * pedmas whatever you doing to it additon subtraction, division, multiplication etc
