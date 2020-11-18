# List: [list]
# Dictionary : 
# Tuple: ()

#Tuple - index itself is immutable
#list - idex is muteable

post = ('Python Basics', 'Intor guide to pyton', 'Some cool python content') #tuple cant sort a tuple 
post = ['Python Basics', 'Intor guide to pyton', 'Some cool python content']#list if the order of the elements change so will the output,
# suddenly the unpacking doest make sense
# this is called tuple unpacking makes it faster to do it
title, sub_heading, content = post
post.sort()
# index way of doing it 
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)