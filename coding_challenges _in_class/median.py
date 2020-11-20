# import math

 
# # sort the list 
# # find the center of the list if its odd use the math.floor function to do it 
# # print the list  

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]


# # def find_median(li):
#     # median = len(math.floor(li%2))
# sort_list = sorted(sale_prices)
# length = len(sort_list)
# median_index = length / 2 
# median = slice(math.floor(median_index:))
# print(median)

sale_prices = [
  100,
   83,
   220,
   40,
   100,
   400,
   10,
   1,
   3
 ]
 sorted_list = sorted(sale_prices)
 num_of_sales = len(sorted_list)
 first_sales_items = sorted_list[:math.floor(num_of_sales/2)]
 last_sales_items = sorted_list[]



 import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)

import math
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3,
  9,
  15,
]
def median_odd(num_list):
  if len(num_list) % 2 == 0:
    return "List must have odd number it elements"
  sorted_list = sorted(num_list)
  list_length_mid = len(sale_prices) // 2
  return sorted_list[list_length_mid]
print(median_odd(sale_prices))




    
    


