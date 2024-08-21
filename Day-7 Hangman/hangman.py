word_list = ["refat","reshad","lipa","nurul"]
# Random choice
import random
choosen_word = random.choice(word_list)
print(choosen_word)

word_length = len(choosen_word)
display = []
for position in range(word_length):
    display += "_"
print(display)

# Guess the user 
end_of_game = False
life = 6
while not end_of_game:
    guess = input("Please enter a guess letter : ").lower()

    
    for position in range(word_length):  # it will show thae number
        # hold the cuurent letter in the choose word and we know position
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in choosen_word:
        life -= 1
        if life == 0:
            end_of_game = True
            print("u lose")
            
    # print(display)
    print(f"{''.join(display)}")
    print(f"Life remain {life}")
    if "_" not in display:
        end_of_game = True
        print("you win!")