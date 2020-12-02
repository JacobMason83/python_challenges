import functools
from functools import reduce

def average_of_list(num_list):
     sum_of_list = reduce(lambda a , b: a + b, num_list) accumulater is a and b
     length_of_list = len(num_list)
     return sum_of_list / length_of_list


    
def average_of_list(num_list):   
    length = len(num_list)
    total = 0
    
    for num in num_list:
        total += num
        
    average = total / length
    return average
        
    
    
    


num_list = [1,2,3,4,5,6]
print(average_of_list(num_list))