import random
def deal_card():
    """Returns a random card"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_card(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    new_card = deal_card()
    user_card.append(new_card)
    computer_card.append(new_card)

user_score = calculate_card(user_card)
computer_score = calculate_card(computer_card)
print(f"Your card {user_card} , current score: {user_score}")
print(f"Computer first card {computer_card[0]} ")
if user_score == 0 and computer_score == 0 and user_score > 21:
    is_game_over = True