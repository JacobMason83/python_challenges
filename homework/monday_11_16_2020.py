from functools import reduce
import operator 
#1. Sum all numbers in a list
# EX: [1, 2, 3] => 6
# I want at least 2 solutions here, but shoot for three different answers here:
def sum_numbers(li): # 1 method and defining the function
    # use the reduce method to add them together 
    return (reduce(lambda a , b: a + b , li))
# print the function 
print(sum_numbers([1,2,3,4,5,6]))

def add_numbers(li): # 2 define the function 
    # set the starting total for the loop aka the initializer
    sum = 0
    # running the for loop to loop thru the list and adding each time you do it 
    for i in li:
        sum += i
        # returning the sum to be printed to the console 
    return sum
    
   

print(add_numbers([1,2,3,4,5,6])) 





#2. Take list of words and return the longest one:
# EX: ["PHP", "Backend", "Exercises"] => "Exercises"
#
# Utilize Pseudo code, it helps you and shows me that you're working through these problems. 
#Naming conventions are important. Let's start getting in the habit of writing good code. Awesome work today d00dz!


# create a function and give it a argument 
def biggest_word(string_list): 
# since its in smallest to biggest because of the sort it should be at the end so if i reverse it it should be at index zero 
    string_list.sort(key=len, reverse=True)

    return string_list[0]
# take the biggest one and return it at the index of zero 

print(biggest_word(["PHP", "Backend", "Exercises"])) #should return largest number 
print(biggest_word(["PHP", "Backend", "Exercises"])) #should return largest number 
print(biggest_word(['Supercalifraglisitcexpialidious', "Backendserversystemgogogogogo", "Exercises"])) #should return largest number 