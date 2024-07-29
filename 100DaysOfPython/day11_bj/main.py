## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random as ran
# we need cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#deal cards function
def deal_cards():
    userHand = ran.choices(cards, k=2)
    computerHand = ran.choices(cards, k=2)
    return userHand, computerHand
def single_draw(hand):
    hand.append(ran.choice(cards))
def hand_sum(hand):
    total = sum(hand)
    num_aces = hand.count(11)   
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total
userCards, compCards = deal_cards()
game_over = False
while not game_over:
    print(f'user cards {userCards}: {hand_sum(userCards)}')
    choice = input('do you want to (h)it or (s)tay? h/s: ')
    if choice == 'h':
        single_draw(userCards)
        if hand_sum(userCards) > 21:
            print(f'Hand {userCards}: {hand_sum(userCards)}')
            print('BUSTED')
            game_over = True
        elif choice == 's':
            break
if not game_over:
    print(f'comp hand {compCards}: {hand_sum(compCards)}')
    while hand_sum(compCards) < 17:
        single_draw(compCards)
        if hand_sum(compCards) > 21:
            print(f'Hand {compCards}: {hand_sum(compCards)}')
            print('Comp busted, you win!')
            game_over = True
if not game_over:
    print(f'final hand {userCards}: {hand_sum(userCards)}')
    print(f'comps hand {compCards}: {hand_sum(compCards)}')
    if hand_sum(userCards) > hand_sum(compCards):
        print('You won')
        game_over = True
    elif hand_sum(userCards) < hand_sum(compCards):
        print('You lost!')
        game_over = True
    else:
        print('Draw!')
        game_over = True