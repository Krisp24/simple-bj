# Importing random module for shuffling the deck

import random


def blackjack():

#Defining all the storage for the game
  
  deck = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]
  user_cards = []
  score = 0
  computer_cards = []
  computer_score = 0

# Printing the game's name
  
  print("Blackjack")

# This shuffles the deck and takes out 2 cards from it, basically (in reality, it shuffles the infinite deck and takes the first card from it twice)
  
  for number in range(2):
    random.shuffle(deck)
    user_cards.append(str(deck[0]))
    score += deck[0]

# Some code that checks if user has an ace and deck value above 21. If true, it turns the ace value into 1, and it removes 10 from the score of the deck.
  
  if "11" in user_cards and score > 21:
    score -= 10
    user_cards[(user_cards.index("11"))] = "1"

# Shuffles user deck and takes first card out of it for dealer's (the computer's) first card
  
  random.shuffle(deck)
  computer_cards.append(str(deck[0]))
  computer_score += deck[0]
  
# Printing the user and dealer's deck
  
  print(f"Your cards: {user_cards}")
  print(f"Dealer cards: {computer_cards}")
  
  
    
# Input for determining whether user wants to hit or stand
  
  user_choice = False  
  user_input = input("Would you like to hit or stand? H or S\n")

# I made the user_input variable not be case sensitive, and it rejects any other string values unless it's the letter "h" or "s"
  
  if user_input.lower() != "h" and user_input.lower() != "s":
        user_input = input("Wrong input. Please type either H or S.\n")

  # When this becomes true, it initiates a while loop for hitting
  
  if user_input.lower() == "h":
    user_choice = True
    
  
  
    
  
    
# While loop for repeating this until user stands
    
    while user_choice:
      
#Shuffles deck and takes first card out for user again
      
      random.shuffle(deck)
      user_cards.append(str(deck[0]))
      score += deck[0]
      
# Same ace checker as above in the code
      
      if "11" in user_cards and score > 21:
        score -= 10
        user_cards[(user_cards.index("11"))] = "1"
    
      print(f"Your cards: {user_cards}")

# if and nested if statements for determining if user busts. User is asked if they want to restart game or not. Game ends if user declines. If user acepts, the game (blackjack() function) restarts.
      
      if score > 21:
        print("You bust. Dealer wins.")
        restart = input("Would you like to play a new game? Y or N. ")
        
        if restart.lower() == "Y":
          blackjack()
          
        elif restart.lower() == "n":
          print("Goodbye")
          
        else:
          print("Wrong input. Goodbye anyways.")
          return
          
# elif statement that warns user to not hit if they get a 21 ( from the goodness of my heart :) )
      
      elif score == 21:
        print("Your score is 21. I advise you to not hit.")

# Another input that asks the user if they want to hit or stand, and the user will exit the while loop if they pick "s"
      
      user_input = input("Would you like to hit or stand? H or S\n")
      
      if user_input.lower() != "h" and user_input.lower() != "s":
        user_input = input("Wrong input. Please type either H or S.\n")
        
      if user_input.lower() == "s":
        user_choice = False


# While loop for the computer that draws cards for them. If dealer doesn't have a hand that has a value less than 17, then it will keep drawing    
  
  if user_input.lower() == "s":
    
    while not computer_score > 17:
  
  # Shuffles inf deck and dealer draws. Basically the same code as above for giving cards to the user
      
      print("Dealer draws.")
      
      random.shuffle(deck)
      computer_cards.append(str(deck[0]))
      computer_score += deck[0]
      
  # Same ace checker as above
      
      if "11" in computer_cards and computer_score > 21:
       
        computer_score -= 10
        computer_cards[(computer_cards.index("11"))] = "1"
  
      
      
      print(f"Dealer deck: {computer_cards}")

      # Basically a whole bunch of conditional statements for dictating whether user wins or not: This one calls the user a winner if the dealer busts, and asks them if they want to play again
      
      if computer_score > 21:
        restart = input("Dealer busts. You win. Want to play another game? Y or N\n")

        if restart.lower() == "y":
          blackjack()
        
        elif restart.lower() == "n":
          print("Goodbye.")
          return
        elif restart != "y" and restart != "n":
          print("Wrong input, game ends. Goodbye.")
          return
      
      # This one checks if the dealer's score is higher than the user's. User loses, and is asked if they want to restart the game
      
      if computer_score > score:
        restart = input("Dealer wins. Want to play another game? Y or N\n")
        
        if restart.lower() == "y":
          blackjack()
        
        elif restart.lower() == "n":
          print("Goodbye.")
          return
        elif restart != "y" and restart != "n":
          print("Wrong input, game ends. Goodbye.")
          return
      
  
  # This conditional statement checks if the dealer busts, user has a better deck than the dealer, or if both the user and dealer have the same deck value
    
    if computer_score > 21:
        print("Dealer busts. You win.")
    
    if score > computer_score:
      print("You win.")
    
    # elif score < computer_score:
    #   print("Dealer wins.")
  
    elif score == computer_score:
      print("Standoff. Draw.")
      
  # After the above conditionals, user is asked if they want to play again or not. 
    
    restart = input("Do you want to play again? Y or N. ")

    if not restart.lower() == "y" and restart.lower() == "s":
      print("Wrong input, so game automatically ends.")
    elif restart.lower() == "y":
      blackjack()
    elif restart.lower() == "s":
      print("Goodbye")
    
    
    
      
   
        
      
  
blackjack()
  

