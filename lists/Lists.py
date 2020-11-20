#is like an array in javascript and other languages
import math
import abc
"""
User Database Query
Kristine
Tiffany
Jordon
"""
#lists in python are not immutable which means they are muteable
users = ['Kristine','Tiffany','Jordon']
# lists are a great way to manipulate the data within the list 
print(users)
#the insert method allows you to add to the list by the zero based index and what your adding 
users.insert(0, 'Anthony')
print(users)
names = 'Jacob', 'Mike', 'Rachel'
#insert places it at a index of 1 with names variable 
users.insert(1, names)
#append adds it to the end of the list
users.append('Johnny')

print(users)
#printing the list of users at index of 2
print([users[2]])
#assinging the index of 4 to Brayden 
users[4]= 'Brayden'
print(users)
users[1]= 'Jacob'
print(users)
#for extend you have to add names via a variable 

names = 'John','Mike','Tina'
users.extend(names)
print(users)
#how to remove items with the remove method with the argument of who you want to remove
users.remove('Mike')
print(users)
# the method of pop it removes the last item in the array/list and removes it and stores that variable 
popped_user = users.pop()
print(popped_user)
print(users)
#delete users from the list by using the del method
del users[1:-1]
print(users)
