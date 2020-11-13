heading1 = 'Python: An Introduction, and Python: Advanced'

header, _, subheader = heading1.partition(': ')

notes = """
 partition returns a tuple and will return a variable deconstruction, the first will go into header, then 2nd will go into _ 
  and third will get subheader
"""
 #print(header)

 #print(subheader)
first, second, third = heading1.partition(': ') 
 # (': )  is a dilemeter saying anything after that will go into the variable
#  and the (', or an') whatever you want to match to help divide it into 3 values partition takes it into 3rds 

print(first)
print(second)
print(third)

# #split function 
tags = 'python, coding, programming, development' #think of it as tags for yourtube etc 

list_of_tags = tags.split(',')  
# turns this into a collection very easily basically a list 

print(list_of_tags)
# # this splits it by the dilimeter of , 

list_of_tags = tags.split()
# splits into one index instead of 4
print(list_of_tags)
print(list_of_tags[2])

heading2 = "Python: An Introduction"

heading_list = heading2.split()

print(heading_list)

heading_list = heading2.split(': ')

print(heading_list)