# if condition is met , or not is conditionals 
age = 25

if age < 25:
    print(f'Im sorry you need to be atleast 25 years Old ')
elif age > 100:
    print(f"Im sorry, {age} is too old to rent a car")
else:
    print(f'Your good to go, {age} fits in the range to rent a car. ')
    
#ternary operators 

role = 'admin'

auth  = 'can access' if role == 'admin' else 'cannot access' 
# can make it hard to understand as well makes it easier to read and understand this way

print(auth)

if role == 'admin':
    auth = 'access'
else: 
    auth = 'cant access '
    
#conditional operators in python 
# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated) shouldnt use it at all , if you run into this is 
# it is another way you used to be able to check for inequality 
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

# username = 'jonsnow'

# if username == 'jonsnow':
#   print('Welcome Jon')
# else:
#   print('You shall not pass!')

# age = 25

# # if age <= 25:
# #   print(f"I'm sorry, you need to be at least 25 years old")
  
# # user_list = ['Kristine', 'Tiffany',]
# # second_list = ['Jordon', 'Brayden']

# # if user_list == second_list:
# #     print('They Match!!')
    
# # sentence = 'The quick brown fox jumped over the lazy dog'
# # word = 'quick'

# # if word in sentence:
# #     print('The word was found in the sentence')
# # else: 
# #     print('The word was not in the sentence')
# # # the if in conditional 

# # Compound conditionals 

# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'

# if username == 'jonsnow' and password == 'thenorth':
#     print('Access Permitted')
# else:
#     print('You shall not pass!')
#     #wouldnt recommend no reason to nest it and just use and operator
# if username == 'jonsnow' :
#   if password == 'thenorth':
#     print('Access Permitted')
# else:
#     print('You shall not pass!')
# #gives you greater flexability 
# if username == 'jonsnow' or password == 'thenorth':
#     print('Access Permitted')
# else:
#     print('You shall not pass!')
# #using both and and or operators 
# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#     print('Access Permitted')
# else:
#     print('You shall not pass!')

logged_in = True 
standard_user = True
#and not means if logged in and is not a standard user 
if logged_in and not standard_user:
    print('You can access the admin dashboard')
else: 
    print('You can only access the standard dashboard')