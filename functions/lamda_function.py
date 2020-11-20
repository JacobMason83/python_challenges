from functools import reduce
#lambda will wrap up fuctionality and be used somewhere else, it allows you to wrap up a process, returns a value
full_name = lambda first, last: f'{first} {last}'


# def greeting(name):
#     print(f('Hi there {name}'))
    
# greeting(full_name('Kristine', "Hudgens"))# lambda allows you to wrap up an entire function and wrap it up in one line and use it elsewhere

def reduce_1(function, collection):
    
    print(function)
    total = 0
    
    for i in collection:
        total = function(total, i )
        
    return total 


print(reduce_1(reduce(lambda x, y: x +y, [1,2,3,], 1),[1,2,3]))

# def new_one():
#     return   reduce(lambda x, y: x+y, [], 1)

# print(new_one())
