# List: [list]
# Dictionary : 
# Tuple: ()

#Tuple - index itself is immutable
#list - idex is muteable

 #tuple cant sort a tuple 
# post = ['Python Basics', 'Intor guide to pyton', 'Some cool python content']#list if the order of the elements change so will the output,
# # suddenly the unpacking doest make sense
# # this is called tuple unpacking makes it faster to do it
# title, sub_heading, content = post
# post.sort()
# # index way of doing it 
# # title = post[0]
# # sub_heading = post[1]
# # content = post[2]

# print(title)
# print(sub_heading)
# print(content)
#how to leverage reassignment to alter a tuple 
# how to add published to a tuple 
post = ('Python Basics', 'Into guide to pyton', 'Some cool python content')
# when you have just parens it will think of it as a mathmatical evaluation 
post = post + ('published',) #adding a comma here will allow it to be added to a tuple , without
# it , it would throw an error , so you can add whatever you want to it as long as it has a comma after the last item 

tags = ['python', 'coding', 'tutorial']
post += (tags,)
# print(post[-1][1])
print(post[1::2])# you can slice just like a list 
#how to remove items from a tuple
#by def its not muteable its immutable what this is , is a hack
#how to remove items from the end of the end of the tuple
# first way is to slice , its nice and clean way to do it 
post = post[:-1]
print(post)
#how to remove the element from the beginning of the tuple
post = post[1:]
print(post)
# situation if you didnt create it , and you need to manipulate it , then use this messy method/not recommended
# method of removing a specific element by casting to a list and  treat it like a list
post = list(post)
post.remove('published')
post = tuple(post)
print(post)
# how to use tuples as dictionarys 
priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}
print(list(priority_index.keys()))
