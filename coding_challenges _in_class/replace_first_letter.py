# Replace all the occurencies of the first letter in the string with '$' except for the first letter itself

# my_string = 'racecar'
# new_string =my_string.replace('r', '$')

# print(my_string[0].join(new_string))

def char_replace(string):
    replace_value = string[0]
    second_half = string[1:]
    new_string = f'{replace_value}{second_half.replace(replace_value, "$")}'
    print(new_string)

def first_replace(string):
    replacement_list = ""

for i in string[1:]:

    if i == string[0]
        replace_list.append(i)

    else: 
        replace_list.append(i)

return f'{string[0]}{"".join(replacement_list)}'
        