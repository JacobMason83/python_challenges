#random sort order , it just doesnt care about it , and ascii applys to this and 
tags = {
    'python',
    'coding',
    'tutorials'
}
# whenever you use a set it has unique properties , 
# and say if you have a duplicate data itll skip over it and show all the unique properties
print(tags)

#print(tags[0]) nope dont work 
#gives a nice syntax to see if something exist in the set 
# you will be able to check to make sure something went into the set 
query_one = 'python' in tags
query_two = 'ruby' in tags  

print(query_one)

#common functions with working with sets 
tags_one = {
    'python',
    'coding',
    'tutorials',
    'coding'
}
tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# Merged Tags uses the pipe char to merge them its the bitwise characters

# merged_tags = tags_one | tags_two

#tags in tags_one but not in tags_two  and takes away all the 
# common tags in one and two and return only that tags in tag_one

# exclusive_to_tag_one = tags_one - tags_two
# exclusive_to_tag_two = tags_two - tags_one
# print(exclusive_to_tag_one.
# print(exclusive_to_tag_two

#tags found in both tags_one and tag_two looking for *** only*** the shared items

universial_tags = tags_one & tags_two
print(universial_tags)

# commonly used for like email lists and or sign-ups and use bitwise operators 
