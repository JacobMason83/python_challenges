tags = [
    'python',
    'development',
    'tutorials',
    'code',
    'programming'
    ]

    # slice has alot of varations on it but here is one of them 
# slice_obj = slice(2)

print(tags[1:4:2]) #same as slice 
#different varations start has the attribues of start stop and step 
slice_obj = slice(1, 4, 2)
#good for calling on it on different data sets



print(tags[slice_obj])
print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)