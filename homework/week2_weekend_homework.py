# # What is List Comprehension in Python? it is a way to run a for loop on one line. like var = [num for num in numbers: if ...]
# # What is a Python Conditional and what is it used for? a python conditional is an if else elif statement that can be used to put logic into your programs
# # What is the difference between returning and printing a value from a python method/function? printing is printing to the console, and returning is storing the variable to be used by other functions
# # What is a default argument? Explain a use case. default arguement is as it sounds the default arg for the function if nothing is put in like 
# def greeting(name, last = 'is a cool cat'):
#     print(f'Hi {name}{last}')
     
# print(greeting('Jacob')) // will print Jacob is a cool cat
# # What is a named argument? a named arguement is a as it sounds its named so when you call the greeting function i would say name="jacob" last="Mason"
# # What does the *args  do in a python function and how might you use it? args allows for more than one thing to be in that argument it basically unpacks everything that you put into it thats what the * does
# # What are Keyword Arguments in Python? keyword args are keywords or *kwargs and is used when you dont know what your 
# # gonna put into it but you use named arguements to put it into the function and to do this you use the *kwargs syntax as your arguement


# Write a program that separates each character of a string by a hyphen. Each character should accumulate based on the current iteration count. The start of each accumulated value should be capitalized. 
# IE:  "abcd" => "A-Bb-Ccc-Dddd"
#      "RqaEzTy" => "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"

def hyphen_accumalator(string): # the name of the function im running the process thru 
    #setting the count of the accumulator
    count = 0
    # making an empty list  for appending my string 
    li_two = []
    # running the for loop on the string 
    for i in string:
        # adding to the count every iteration 
        count += 1
        # appending to the list  the count at the iteration moment and multiplying it by the char at i , and then capitalizing it 
        li_two.append(str(count * i).capitalize())          
        # returned the joined list and returning it 
    return'-'.join(li_two)  
         
print(hyphen_accumalator('abcdefg'))
print(hyphen_accumalator('johnny'))
print(hyphen_accumalator('ryan'))
print(hyphen_accumalator('donald'))




