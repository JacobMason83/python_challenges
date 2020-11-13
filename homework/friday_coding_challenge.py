# Write a program that will make any number negative

def is_it_negative (number):
    if number < 0:
        return number
    elif number == 0:
        return 'its neither negative or positive' 
    else :
        return (-1) * (number)

print(is_it_negative(12))
print(is_it_negative(55))
print(is_it_negative(-56445654562165656496496))
print(is_it_negative(0))
print(is_it_negative(12))

# to check if its a positive number

def is_it_positive (number):
    if number < 0:
        return abs(number)
    elif number == 0:
        return 'its neither negative or positive' 
    else :
        return number

print(is_it_positive(-13))
print(is_it_positive(0))
print(is_it_positive(-56896589552665646546464))
print(is_it_positive(-13))
