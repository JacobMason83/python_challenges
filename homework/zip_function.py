#how to leverage the powerful python zip function
# make sure your lists are sorted correctly 
positons = ['2b', '3b','SS', 'DH']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
#the zip functions allows you to take two lists and merge them into a tuple, 
# and your maintaining the pairs of data via the zip function 
scoreboard = zip(positons, players) #returns zipped object finds all matching items in the list***
# in order to use zip you need to have the same amount of items in the list 
#always have to cast it to a list to print or use it 
print(list(scoreboard))

