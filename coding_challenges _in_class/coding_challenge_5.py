# define a function take a letter and a number 
# and multiplies the number and multiplies by $ 
# return g as the key 
histogram = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12
}
def histogram_maker(name, amount):
    histogram = {}
    dollar_sign = '$'
    value = dollar_sign * amount  
    histogram[name] = value

    return histogram
    





print(histogram_maker('google', 20))
print(histogram_maker('yahoo', 30))
print(histogram_maker('My future account', 1))
print(histogram_maker('My wifes future account', 40))
print(histogram_maker('Ben and Jerrys ', 50))
print(histogram_maker('Kroger', 10))

# also can do it is way 
sales = {
    'google': 20,
    'facebook': 42,
    'twitter': 10,
    'offline': 12
}
print('g' + sales[google] * '$')
print('f' + sales[facebook] * '$')
print('t' + sales[twitter] * '$')
print('o' + sales[offline] * '$')
