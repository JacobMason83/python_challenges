api_data = '5'
greeting = "Hi"
# if it has a space in it will fail in isaplpha() checking if its a  alphanumeric character , spaces fail 
print(api_data.isalpha())
print(greeting.isalpha())

# checking to see if it is a number actual alphanumeric character
print(api_data.isnumeric())
print(greeting.isnumeric())

num = '(555) 867-5309'

print(num.strip('( ' ')' ' ' '-'))

