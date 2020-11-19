num_list = range(1,11)
# cubed_nums = []
# traditional method 
# for num in num_list:
#     cubed_nums.append(num **3)
# non traditional way always needs to be stored in a value?
#  cubed_nums = [num ** 3 for num in num_list]  
#  num **3 is what your wanting the loop to do  
# num is the iterator 
# num_list is the container your pulling from 

# will build a list that will capture even numbers 
# first will be the for in loop and the 2nd one is the list  comprehension way 
# even_numbers = []

# for num in num_list:
#     if num % 2 ==0:
# #         even_numbers.append(num)
#  first num is the variable/iterable variable 
#  for num in num_list is the container were checking 
# #  if is the conditianal were checking        
even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)