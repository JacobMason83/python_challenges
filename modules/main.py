import sys
sys.path.insert(0,'./libs') #tells python to look in the current directory and will pull in all the current working directory 
# and you can also use the original folder 

import helper

def render():
    print(helper.greeting('Jacob', 'Mason'))
    
render()