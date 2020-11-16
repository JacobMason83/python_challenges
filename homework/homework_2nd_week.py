import math
import abc
from functools import reduce


# 1) Given a list, concatenate the elements and return a string.
# EX: ['h', 'i', 5] => 'hi5'

some_list = ['h', 'i', 5]

new_list = ''.join(str(elem) for elem in some_list)
print(new_list)
 
#iterative approach 
def concat_list(li):
    string = ""
    for element in li:
        string += element

    return string

print('h', 'i', 5)

# 2) Sort a string and return it in alphabetical order
# EX: "Hi There" => "eehhirt"

# my_string = "Hi there"


def sorted_string (str): #this solution is  better
    string = str.strip(' ').lower()
    return ''.join(reduce(lambda a, b: a + b , sorted(string)))



# def sorted_string(my_string): #this solution works as well 
#     my_string = my_string.lower()
#     sorted_string = sorted(my_string.strip(' '))
#     my_string = ''.join(sorted_string)
    
#     return my_string
  # def sort_string (string):
  # return "".join(sorted(string, key=lambda x:.lower())).strip())   this is making it easier  

print(sorted_string("Hi there brfrom functools import reduceoham"))
print(sorted_string("I love the way you lie"))
print(sorted_string("cdjdabfdnlaknvljnljhojhddidinnniueotudcnh"))
print(sorted_string("cba"))
print(sorted_string("Hi There")) 


# 3) Write a program that splits a hyphen separated string, and returns a new hyphen separated string where the words are in alphabetical order.
# IE: "green-red-black-white" => "black-green-red-white
   
def hyphen_string(string):
    hyphen_string=[a for a in string.lower().split('-')]
    hyphen_string.sort()
    return('-'.join(hyphen_string))

def hyphenated_string(string):
    hyphen_str = string.lower().strip("-")
    new_list = sorted(hyphen_str)
    return '-'.join(new_list)
print(hyphen_string("green-red-black-white"))
print(hyphenated_string("green-red-black-white"))

