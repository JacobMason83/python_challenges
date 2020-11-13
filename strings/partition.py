heading = 'Python: An Introduction, and Python: Advanced'

header, _, subheader = heading.partition(': ')

# partition returns a tuple and will return a variable deconstruction, the first will go into header, then 2nd will go into _ 
# and third will get subheader

# print(header)

# print(subheader)
first, second, third = heading.partition(': ') #(': )  is a dilemeter saying anything after that will go into the variable
# and the (', or an') whatever you want to match to help divide it into 3 values partition takes it into 3rds 

print(first)
print(second)
print(third)