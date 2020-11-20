# named arguments 
def full_name(first, last):
    print(f'{first} {last}')
    
full_name(first='Kristine', last='Hudgens') #being much more explict with the function and to python by the named arguments
#also can do this as well
full_name (last='Hudgens', first='Kristine') #mapping needs to match up , but when using named arguements it allows to be more explicit with it
# rule of thumb if you have 2 or more arguements then use named arguements 

def greeting(time_of_day, *args):
    print(f"Hi  + {' '.join(args)}, I hope your having a good {time_of_day}") # join joins the values into a string 
    # * brings in all the elements in args into the function . args is just a naming convention in python 
    # print(args)
    
greeting('Morning','Tiffany', "Hudgens")
greeting('Afternoon', 'Tiffany', 'M',  "Hudgens")

#keyword arguments
