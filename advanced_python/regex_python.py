#regular expressions used to grab certain files 
import fnmatch
from fnmatch import fnmatchcase
import os
def list_files():
    for file in os.listdir('.'): # list of files function is looping thru the files in that system and match the pattern
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files:", file)
        if fnmatch.fnmatch(file, "*.py"):
            print("Python files:", file)
        if fnmatch.fnmatch(file, "*.rb"):
            print("Ruby files:", file)
        if fnmatch.fnmatch(file, "*.yml"):
            print("Yaml files:", file)
            
# list_files()

#want to filter thru this array and only find 2b in it and pull that out of the file 
#can be used for a real estate site, when you want to filter out streets not blvds or whatever you want 
players = [ 
    "Jose Altuve 2B",
    "Carlos Correa SS",
    "Alex Bregman 3B",
    "Scooter Gennett 2B"
]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B") ]

print("players that play second base: ", second_base_players)

#how to add to a preexisting file

import datetime
from time import sleep

for i in range(5):
    file_builder = open("logger.txt", "a+") # a plus allows you to append the file 
    file_builder.write(f'{datetime.datetime.now()}\n') # brings in the current date and time as  a timestamp 
    
    file_builder.close()  #close the file 

    print("file created") #prints file created and then 
    #sleep for a sec and repeats 5 times 

    sleep(1)
    
    # how to read and working with file data in python 
def get_file_contents(filename): # creates a function for file contents 
    queried_file = open(filename, 'r') # takes 2 arguments , open is taking the filename and r for reading the file 

    if queried_file.mode == 'r': # quality check to make sure that line 51 worked  and to make sure your in read mode and not in another one 
        return queried_file.read() # calling a read function on the queried file 


content = get_file_contents('file-section/text_content.txt') # you need to call the full relative path of the filename in the function 

print(content)

print("Number of words", len(content.split())) # splitting the function and prining the length of the content

#delete 

import os # allows us to interact with the system that were working on 

os.remove("file-section/file_to_be_deleted.txt")

print("File Removed!")