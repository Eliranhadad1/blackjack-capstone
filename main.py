############### Blackjack Project #####################
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def has_Ace(cards):
    while sum(cards) > 21 and 11 in cards:
        index = cards.index(11)
        cards[index] = 1

def check_winning(user_cards, computer_cards):
    if sum(computer_cards) == 21:
        clear()
        print(logo)
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("Computer got Blackjack, you lose!")
        return "Game_end"
    elif sum(user_cards) == 21:
        print("Win with a Blackjack!")
        return "Game_end"
    elif sum(user_cards) == sum(computer_cards):
        print("It's a draw!")
        return "Game_end"
    elif sum(user_cards) > 21:
        clear()
        print(logo)
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You went over. You lose :(")
        return "Game_end"
    if sum(computer_cards) > 21:
        has_Ace(computer_cards)
        check_winning(user_cards, computer_cards)
        

# Generate cards
user_cards = [random.choice(cards),random.choice(cards)]
computer_cards = [random.choice(cards),random.choice(cards)]
should_continue = True
user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if user_choice == 'n':
    should_continue = False
while should_continue:
    clear()
    print(logo)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    result = check_winning(user_cards, computer_cards)
   
    decision = input("Type 'y' to get another card, type 'n' to pass: ")
    if decision == 'y':
        user_cards.append(random.choice(cards))
        has_Ace(user_cards)
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        check_winning(user_cards, computer_cards)
    if decision == 'n':
        while sum(computer_cards)<16:
            computer_cards.append(random.choice(cards))
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer cards: {computer_cards}, current score: {sum(computer_cards)}")
        if sum(computer_cards) > 21:
            print("computer lose, you win!")
        elif sum(user_cards) > sum(computer_cards):
            print("computer lose, you win!")
        else:
            print("Computer win, you lose!")
        break
    if result == "Game_end":
        should_continue = False
        
        should_continue = False


    
        
