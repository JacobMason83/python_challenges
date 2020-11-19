# # players = ['Altuve', 'Bregman', 'Correa', 'Gattis'] this is for lists and tuples

# # for player in players: # players list will print each player player is the iterator 
# #     # common convention say you have a plural collection its common practice to user the singular block variable 
# #     #will work the same as a tuple called players
# #     print(player)
# # dictionaries 
# players = {
#     '2b': 'Altuve',
#     '3b': 'Bregman',
#     'SS': 'Correa',
#     'DH': 'Gattis'
# }

# for position, player in players.items(): # position is the key , and player is the value and 
# #dictionary name .items() allows you to iterate over the dictionary
#   print('Position:', position)
#   print('Player:', player)
# #   for looping thru strings 
#   alphabet = 'abcdefghijklmnopqurstuvwxyz'
#   for letter in alphabet:
#       print(letter)
# name = "Bottega University"  
# def len_one(collection):
#   length = 0   
#   for element in name:
#     length += len(element) 
    
#   return length

# # print(len_one(name))
    
# # numbers = [1,2,3,4,5,6]
# # for i in numbers:
    
# #     i+=1
# #     print(i)
    
# for num in range(1, 10):
#     print(num)
# this is a good way for a block list of usernames or ip address 
usernames =  [ 
'jon',
'tyrion'
'theon',
'cersei',
'sansa'
 ]


for username in usernames:
    if username == 'cersei':
        # print(f'Sorry,  {username}, you are not allowed')
        print(f'{username} was found at index{usernames.index(username)}')
        # continue
        break
    # else:
    #     print(f'{username} is allowed')
    print(username)
    

    

