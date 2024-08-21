alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def caesar(start_text, shift_amount,cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d expected text is {end_text}")

sould_continue = True
while(sould_continue):
    direction = input("direction :")
    text = input("text :")
    shift = int(input("shift :"))

    shift = shift % 26
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input("New 'yes' : 'no' ")
    if result == 'yes':
        should_continue = False
    else:
        should_continue = True
        print("Good bye")