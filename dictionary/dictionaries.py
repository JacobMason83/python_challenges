# players = {
#     'ss': 'Correa',
#     '2b': 'Altuve',
#     '3b': 'Bragmen',
#     'DH': 'Gattis',
#     'OF': 'Springer'
# }
#  #python is very good at giving errors for data issues rather than other languages who will print null
# second_base = players['2b']
# designated_hitter = players['DH']
# out_fielder = players['OF']
# print(players)
# print(designated_hitter)
# print(out_fielder)
# #nested collections within a dictionary 
# teams = {
#      "astros": ["Altuve", "Correa", "Bregman"],
#      "angels": ["Trout", "Pujols"],
#      "yankees": ["Judge", "Stanton"]
#  }
#  #its all the same data as lists and you can work on it 
# # astros = teams['astros']
# # angels = teams['angels']
# # yankees = teams['yankees']
# # print(astros)
# # print(angels)
# # print(yankees)
# # how to add new key:value pairs to dictionaries 

# teams['red sox'] = ['Price', 'Betts']
# print(teams)
# #get function in python 
# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ['Price', 'Betts'],
# }

# featured_team = teams.get('lovers', 'No featured team')

# print(featured_team)

# Python Dictionary View Objects you dont have to understand them you just know how to work with them and see them 
# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }
# # this is way to cast the dictionary view to a list  and then you can manipulate it and make it thread safe, so you dont
# # compromise the original list this is only stored and access for us to use even if someone is updating it .. 
# #brings this back in a tuple 
# player_names = list(players.copy().values())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }
# #value vs refrence later in the program 
# # this will return a tuple and it will say dict_items in front of it to know that its veiw objects
# team_groupings = teams.items()

# """
# [
#   ('astros', ['Altuve', 'Correa', 'Bregman']),
#   ('angels', ['Trout', 'Pujols']),
#   ('yankees', ['Judge', 'Stanton']),
#   ('red sox', ['Price', 'Betts'])
# ]
# """

# print(list(team_groupings))
# #this is what is returned when you cast list to team_groupings 
# """
# [('astros',['Altuve','Correa','Bregman']),
# ('angels',['Trout','Pujols']),
# ('yankees',['Judge','Stanton']),
# ('red sox',['Price','Betts'])]
# """
# print(list(team_groupings)[1][1][1])
# adding to the dictionary is name['key'] = 'new value'
#how to delete data from the dictionary  two ways delete and pop 

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }
# # Deletes it from the dictionary and would throw an error if you didnt have the key in the dictonary 
# del teams['angels']
# removed_team = teams.pop('mets', 'Team not found')

# print(teams)
# print(removed_team)
# guid to nested items in dictionaries 
#teams is a list with multiple dictionaries and fir
teams = [
  {
    'astros': {
      '2B': 'Altuve', # these are going to be exactly like you will be using in api data and stuff like that 
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0]) and would return astros dictionary 

angels = teams[1].get('angels', 'Team not found') #be a good dev and set a default to error check 
# this is going to show a "dictionary view of the list "  
print(list(angels.values())[1])
