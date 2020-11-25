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