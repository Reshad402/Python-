import random
from value_higher_lower import data

def formet_data(account):
    """Returns the data values of the account"""
    acc_name = account["name"]
    acc_description = account["description"]
    acc_country = account["country"]
    return f"{acc_name},  {acc_description} , {acc_country}"

def answer(guess , a_follwer, b_follwer):
    """Returns the answer vai checking"""
    if a_follwer > b_follwer:
        return guess == "a"
    else:
        return guess == "b"
score = 0
game_should_run = True

acc_b = random.choice(data)

while game_should_run:
    acc_a = acc_b  # answer true hole last value ta diyea gain check
    acc_b = random.choice(data)
    if(acc_a == acc_b):
        acc_b = random.choice(data)

    print(f"Compare A : {formet_data(acc_a)}")
    print(f"Compare B : {formet_data(acc_b)}")

    guess = input("Who has more follwers 'A' & 'B' ? ").lower()

    a_follwer_count = acc_a["follower_count"]
    b_follwer_count = acc_b["follower_count"]
    is_correct = answer(guess , a_follwer_count , b_follwer_count)


    if is_correct:
        score += 1
        print(f"You are right . Current Score {score}")
    else:
        game_should_run = False
        print(f"You are wrong . Current Score {score}")