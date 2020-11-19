# find the median of a list with an even amount of elements
# sort list low to high
# 2 middle nums 
# sum of 2 mid nums 
import math 
# li = [1,2,3,4,5,6]
# def even_num_median(li):
#     median = []
#     median.sort(key=int)
#     for num in li:
#       num += 1
      
      
# def find_median(even_num_median(li))
#      return li[num] 
    
      

    
    

# print(find_median(even_num_median(li)))
sales_prices = [100,83,55,33,44,65,66,98,66,55,33,44] 

sorted_list = sorted(sales_prices)

mid_nums_first = len(sorted_list)// 2 -1 
mid_nums_second = len(sorted_list)//2
value_one = sorted_list[math.floor(mid_nums_first)]
value_two = sorted_list[math.floor(mid_nums_second)]
median = (value_one + value_two) / 2
