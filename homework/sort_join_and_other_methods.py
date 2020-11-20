# tags = ['python', 'development', 'tutorials', 'code']

# print(tags)

#  #has all the elements in alphabetical order from a-z would call the oldest one 
# tags.sort()
# #has all the elements in alphabetical order from z=a would call the oldest one 
# tags.sort(reverse=True) 
# print(tags)

# totals = [234, 1, 543, 2345]

# totals.sort() # from lowest to highest
# totals.sort(reverse=True) # from highest to lowest

# print(totals)
#.join method in python 

#search string in the browser that we are gonna use for this query
# https://www.google.com/search?q=python+tutorial  this gives us information on how to write these queries used for 
# #webscrapers and stuff like that and no spaces 

uri = 'https://www.google.com/search?q=python+development+tutorial'
 #uri is very simalar to url and have to be dynamic when building it cause we dont know how many search terms we will have 
tags = ['python', 'development', 'tutorial']
#we need python to know what to search for so in join we put the + sign so it knows what to join together
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}' 
# best way to learn something in programming languages you learn the inputs and outputs and how they work

print(query_uri)
# ranges in python from one index to another index

# tags = ['python', 'development', 'tutorials', 'code']

 # is from index one up to index , so its upto but not including and also if you put [:] itll print everything in that list 
# tag_range = tags[1:2]
# print(tag_range)
# more advanced techniques in ranges with slice in python lists 

tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming',
    'computer science'
]

# tag_range is taking from the beginning to not including -1 and everyother element is the 2 
# tag_range = tags[:-1:2]
# this is taking the list and reversing it very straight forward very easy 
tag_range = tags[::-1] 

# print(tag_range)
# tags.sort(reverse=True) 
#looks at the alphabetical value returns 'tutorials', 'python', 'programming', 'development', 'computer science', 'code'

print(tag_range)
# doesnt sort it it in its own variable it changes the tags variable instead of put into its own variable 
sorted_tags = tags.sort(reverse=True) 

print(sorted_tags)