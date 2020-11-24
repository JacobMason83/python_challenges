# write a program that prints the sum of all number type values in a given dictionary
# ex {'data_1': 100, 'data_2': "100", 'data_3': "150", 'data_4': 10}

def sum_of_num_types(dict):       
    li2 = []
    # looping over the dictionary 
    for  value in dict.values():
        # if the type of value is a int then append to the list 
        if type(value) == int:
            li2.append(value)
            # if type is a float then append the value 
        elif type(value) == float:
            li2.append(value)
        else:
            continue
    return sum(li2)
dict = {
    'data_1': 100,
    'data_2': "100",
    'data_3': "150",
    'data_4': 10
        }
print(sum_of_num_types(dict))

def sum_of_num_types(dict):       
    li2 = []
    # looping over the dictionary 
    for value in dict.values():
        # if the type of value is a int then append to the list 
        if type(value) == int or  type(value) == float:
            li2.append(value)
            # if type is a float then append the value                    
        else:
            continue
    return sum(li2)

#or 
def sum_of_num_types(dict):
    return sum([i for i in dict.values() if type(i) == int or type(i) == float])

print(sum_of_num_types(dict))
print(hasattr(dict, 'data_2'))