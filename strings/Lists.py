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
