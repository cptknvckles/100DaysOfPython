import random as r 
import os

def clear_screen():
    os.system('clear')

    
def draw_initial_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = r.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, comp_score):
    if user_score == comp_score:
        print('Draw 🙃')
    elif comp_score == 0:
        print('AI got BlackJack 🤣')
    elif user_score == 0:
        print('you got blackjack! 😍')
    elif user_score > 21:
        print('You lost! 😭')
    elif comp_score > 21:
        print('AI busted!, you win')
    elif user_score > comp_score:
        print('you win')
    else:
        print('you lost')
def play_game(): 
    user_cards = []
    comp_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(draw_initial_card())
        comp_cards.append(draw_initial_card())
    #this is a while loop for the user 
    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f'Your cards {user_cards}: {user_score}')
        print(f'Comps hand {comp_cards[0]}')
        if comp_score == 0 or user_score > 21:
            is_game_over = True
            if user_score == 0:
                print('You got BlackJack, winner!')
        else: 
            draw_card = input('do you want to hit or stay (h/s):  ')
            if draw_card == 'h':
                user_cards.append(draw_initial_card())
            else:
                is_game_over = True
            
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(draw_initial_card())
        comp_score = calculate_score(comp_cards)

    print(f'your final hand {user_cards}: {user_score}')
    print(f'Computers final hand {comp_cards}: {comp_score}')
    print(compare(user_score, comp_score))
while input('Do you want to play a round of BlackJack? y/n') == 'y':
    print('------------------------------')
    play_game()
