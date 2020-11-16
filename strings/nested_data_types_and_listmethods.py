users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1,2,3,4]
#lists can have multiple data types and you can manipulate it to get what you want out of it this list has nested data types
mixed_list = [43, 10.3, 'Altuve', users] #can be pretty dangerous best practice 
#is to have all of the same data types and would break your code so keep the same data types just be careful!!!!!!

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)
#if you want to query a database keep your lists a uniform as possible 
nested_lists = [[123], [234], [345]]
#list methods starts here and trying to get us closer to what we will be doing in the future!!
#len() length method 
tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
#off by one error and that is because students dont use the zero index correctly 
#2ways of finding the last index number of it 
last_item = tags[-1]
index_of_last_item = tags.index(last_item) #returns the index of the last item 
print(number_of_tags)
print(last_item)
print(index_of_last_item)