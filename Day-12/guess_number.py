from random import randint
random_number = randint(1,100)
print("Random number", random_number)

mode = input("choose 'easy', 'medium', 'hard' ->")

if mode == 'easy':
    life = 10
elif mode == 'medium':
    life = 5
elif mode == 'hard':
    life = 3

guess = int(input("Guess a number between 1 to 100"))
while life > 0:
    if guess == random_number:
        print("You win")
        break
    else:
        life -= 1
        if life == 0:
                print(f"You loss the game the value is {random_number}")
                break
        if(random_number > guess):
            guess = int(input("The number is greater that the number"))
        else:
            guess = int(input("The number is smaller than the number")
            )
            

    