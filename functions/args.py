# # named arguments 
# def full_name(first, last):
#     print(f'{first} {last}')
    
# full_name(first='Kristine', last='Hudgens') #being much more explict with the function and to python by the named arguments
# #also can do this as well
# full_name (last='Hudgens', first='Kristine') #mapping needs to match up , but when using named arguements it allows to be more explicit with it
# # rule of thumb if you have 2 or more arguements then use named arguements 
# #returns the args in a tuple 
# def greeting(time_of_day, *args):
#     print(f"Hi  + {' '.join(args)}, I hope your having a good {time_of_day}") # join joins the values into a string 
#     # * brings in all the elements in args into the function . args is just a naming convention in python 
#     # print(args)
    
# greeting('Morning','Tiffany', "Hudgens")
# greeting('Afternoon', 'Tiffany', 'M',  "Hudgens")

#keyword arguments
# def greeting(**kwargs): #kwargs returns keyword arguments in a dictionary 
#     if kwargs:
#         print(f"Hi {kwargs['first_name]} {kwargs['last_name']}")
#     else: 
#         Print('Hi ' + kwargs)
    
# greeting(first_name = 'Kristine', last_name= 'Hudgens')

def greeting(time_of_day, *args, **kwargs):
    print((f"hi {' '.join(args)}, I hope that you are have a great {time_of_day}"))
    
    if kwargs:
        print('Your tasks for the day are: ')
        for key, val in kwargs.items():
            print(f"{key} => {val}")
            
            
greeting('Morning',  # common convention when having multiple positional arguments is to put them on each line 
         'Kristine', 'Hudgens',
         first = "Empy dishwasher",
         second = 'Take pupper outside',
         third = 'Math homework')
def greeting(**args):
    print(args)