
#before 
# def full_name(first, last):
#       return f'{first} {last}'


# kristine = full_name('Kristine', 'Hudgens')

# def greeting(name):
#   print(f'Hi {name}!')


# greeting(kristine)
#after nesting function within a function 
def greeting(first, last):
 def full_name():
    return f'{first} {last}'
    
    
 print(f'Hi {full_name()}')
    
    
greeting('Kristine', 'Hudgens')
#right way 
def greeting(name = 'Guest'):
    print(f'Hi {name}')
    
greeting()
greeting('Kristine')

def some_function(collection = []): # its gonna go to the collection and add 1 to it 
    collection.append(1)
    return collection
print(some_function())
#if i called this in other part of the program
print(some_function()) #[1] if you even if you call this somewhere and python will go where it was made 
#and now you have the collection that will refrence the functions orignal location and add it to that 
