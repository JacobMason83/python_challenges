import sys
sys.path.insert(0, './libs') #tells python to look in the current directory and will pull in all the current working directory 
# and you can also use the original folder 
import numpy as np
import helper as h # called an alias
#you can also be even more implicit and from helper import greeting and it will allow you to import the specific function
# from helper import greeting
def render():
    print(h.greeting('Jacob', 'Mason'))
    
render()
# you can also alias your import calls like import helper as h or whatever you want as long as its not a reseved word ****
num_range = np.arange(16)
print(num_range)
print(num_range.reshape(4,4))
