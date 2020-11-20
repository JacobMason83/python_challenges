# make a game that i can make a bet on on black Jack
import random
from random import randint
# import homework
# from homework import gui
global bet
global wallet 
wallet = 1500

#place your bet
# def new_bet():
#     global bet
#     global wallet
    
#     bet = int(input('Place your bet: '))
#     if bet > wallet:
#         print(f'Your wallet is at {wallet} please change your bet')
#         return start()
    
def start():
  global bet  
  global wallet
#   wallet = 1500
  print(f'You have {wallet} in your wallet, place your bet accordingly')
  bet = float(input('Place your bet: '))
  if bet > wallet : 
    print(f'If you bet {bet} lose youll owe me money, why dont you try again')
    return start()
      
  else:
      print(f'You start out with: {wallet}  and you have placed a bet of: {bet}')
      return start_game(who_wins())

#deal the cards 
def user_card():
    value = random.randint(0, 21)
    print(f"Your total is:  {value}")
    return value

def dealer_card():
    value = random.randint(0, 21)
    print(f"The Dealers total is:  {value}")
    return value
#set the function for the restart function if they say yes by starting it over again 


def start_game(): 
    global bet 
    global wallet   
    return who_wins()
# who wins takes in the dealer and user card functions and global bet and wallet functions 
def who_wins():
    dealer = dealer_card()
    user = user_card()
    global bet
    global wallet
    print(f"""
          ____________________________________
          |                      __Total__   |
          |                      |A      |   |
          |  DEALING             |       |   |
          |  Cards!!!            |       |   |
          |                      |_______|   |
          |                                  |
          |__________________________________|
          """)
    user_bet = bet    
    # conditionals if dealer wins , user wins  then ask if they want to play again 
    if dealer > user:
       wallet -= bet
       print(f"""
          ____________________________________
          |                      _Total___   |
          |                      |        |  |
          |  You Lost!!!         | Card   |  |
          |                      | Value  |  |
          |                      |________|  |
          |                                  |
          |__________________________________|
            The dealers total is: {dealer}
          """)
       print( f'You lost to the dealers {dealer} and you won: {user_bet} and your wallet is now {wallet}')   
       choice = str((input('Would you like to try and beat my program again?: (y/n)')))  
       return restart_options(choice)
       
    elif user == dealer:
        user_winnings = bet
        wallet += user_bet
        print(f"""
          ____________________________________
          |                      _Your ___   |
          |                      |        |  |
          |  You Tied$$$$        |        |  |
          |                      |        |  |
          |                      |________|  |
          |                                  |
          |__________________________________|
            Your total is {user} and the Dealers is {dealer}
          """)
        print( f'You tied with dealer with{user} you won: {user_winnings} and your wallet is now {wallet}')
        choice = str((input('Would you like to try and beat my program again?: (y/n')))
        return restart_options(choice)
               
    elif user == 21:
        user_winnings = bet * 2.5
        wallet += user_winnings
        print(f"""
          ____________________________________
          |                      __Your__    |
          |                      | total |   |
          |  BlackJack!!!        | card  |   |
          |                      |       |   |
          |                      |_______|   |
          |                                  |
          |__________________________________|
           Your Won  {user_winnings}$$$$$$$$$
          """)
        print(f' You hit a BlackJack , You won with {user} and/n you won:  {user_winnings} and your wallet is now {wallet}')
        choice = str((input('Would you like to try and beat my program again?: (y/n)')))
        return restart_options(choice)       
    else:
        user_winnings = bet
        wallet += user_winnings
        print(f"""
          ____________________________________
          |                      __Your__    |
          |                      | total |   |
          |  You Won$$$$         | card  |   |
          |                      |       |   |
          |                      |_______|   |
          |                                  |
          |__________________________________|
           Your Won  {user_winnings}$$$$$$$$$
          """)
        print(f'You won with {user} and you won:  {user_winnings} and your wallet is now {wallet}')
        choice = str((input('Would you like to try and beat my program again?: (y/n)')))
        return restart_options(choice)

def restart_options(choice):
    global bet
    global wallet
   
    if ((choice == 'y') or (choice == 'yes')):
      return start()
    elif (choice.lower() == 'no') or (choice.lower() == 'n'):
        print('Thank you for playing my game today, I made this game for people to enjoy, I hope you enjoyed my hard work!!!')
        return exit()
    else:
        print("You didnt put a yes or no , Time to play a game!!!! ")
        return start()

#need to add a bet feature that says if you try and bet more than
#  what you have then if you have a negative balance you owe me 

start()











