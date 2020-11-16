tags = ['python', 'development', 'tutorials', 'code']

# Nope performed an override instead of adding on to it 
tags[-1] = 'Programming'

# In Place actually adding on to the tags list
tags.extend('Programming')

# New List it changes tags in place not in a new list 
new_tags =tags.extend(['Programming'])
#if you tried just a string it would have caused an error, by adding the blocks to it it becomes a list 
new_tags = tags + ['Programming']

print(new_tags)

print(tags)