#ChatGPT looked over my code and added slight enhancments lol added more emojis and proper grammar

import random as r


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
        print('You got BlackJack! 😍')
    elif user_score > 21:
        print('You lost! 😭')
    elif comp_score > 21:
        print('AI busted! You win! 😊')
    elif user_score > comp_score:
        print('You win! 🎉')
    else:
        print('You lost! 😢')

def play_game():
    user_cards = []
    comp_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(draw_initial_card())
        comp_cards.append(draw_initial_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f'Your cards: {user_cards}, current score: {user_score}')
        print(f'AI\'s showing card: {comp_cards[0]}')

        if comp_score == 0 or user_score > 21:
            is_game_over = True
            if user_score == 0:
                print('You got BlackJack! Winner! 😍')
        else:
            draw_card = input('Do you want to hit or stay? (h/s): ')
            if draw_card == 'h':
                user_cards.append(draw_initial_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(draw_initial_card())
        comp_score = calculate_score(comp_cards)

    print(f'Your final hand: {user_cards}, final score: {user_score}')
    print(f'AI\'s final hand: {comp_cards}, final score: {comp_score}')
    compare(user_score, comp_score)

while input('Do you want to play a round of BlackJack? (y/n): ') == 'y':
    print('\n * 20')
    print('------------------------------')
    play_game()
