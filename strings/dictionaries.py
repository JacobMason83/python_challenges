players = {
    'ss': 'Correa',
    '2b': 'Altuve',
    '3b': 'Bragmen',
    'DH': 'Gattis',
    'OF': 'Springer'
}
 #python is very good at giving errors for data issues rather than other languages who will print null
second_base = players['2b']
designated_hitter = players['DH']
out_fielder = players['OF']
print(players)
print(designated_hitter)
print(out_fielder)
#nested collections within a dictionary 
teams = {
     "astros": ["Altuve", "Correa", "Bregman"],
     "angels": ["Trout", "Pujols"],
     "yankees": ["Judge", "Stanton"]
 }
 #its all the same data as lists and you can work on it 
# astros = teams['astros']
# angels = teams['angels']
# yankees = teams['yankees']
# print(astros)
# print(angels)
# print(yankees)
# how to add new key:value pairs to dictionaries 

teams['red sox'] = ['Price', 'Betts']
print(teams)
