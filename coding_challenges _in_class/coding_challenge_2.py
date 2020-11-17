import math
import random
from random import randint
from random import choice
# from numpy import np


weights = {
    'winning': 1,
    'losing': 2
}
# other_weights = {
#     'winning': 1,
#     'break_even': 2,
#     'losing': 3
# }

# def weighted_lottery(weights):
#     # you have to do a random pick of the number btween 1 and 1000 then it will return based on weights 
#    new_list = list(weights)
#    length = len(new_list) -1
#    random_value = random.randint(0, length)
# #    looping thru dictonary
#    for i in weights:           
#       return f'You are a {new_list[random_value]}'
  

# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
# print(weighted_lottery(weights))
#actual answer 


# def weighted_lottery(weights):
#     container_list = []

#     for (name, weight) in weights.items():
#         #this is saying that it will loop thru that many times
#         for _ in range(weight): #wehen you put the _ as the value it dont matter the value , we need it there so there is a place to put the items
#             # container_list.append(name) building up a container list for us to store the key name 

#           return random.choice(container_list)

#   i want it to go thru losing it 1000 times rather 
weights = {
     'winning': 1,
     'losing': 1000
 }

# print(weighted_lottery(weights))

other_weights = {
    'green': 1,
    'yellow': 2,
    'red': 3
}

# print(weighted_lottery(other_weights))


#my teachers solution 
def weighted_lottery(weights):
    container_list = []

    for key, value in weights.items():
        for _ in range(value):
            container_list.append(key)
    return random.choice(container_list)

print(weighted_lottery(weights))   

