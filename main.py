alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet_cap =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

from art import logo

print(logo) 


def caesar(direction, plain_text , shift_amount):
    new_word =''
    for letter in plain_text:
        if letter not in alphabet:
            new_word += letter
        else:
            index = alphabet.index(letter)
            if direction == 'encode':
                if (index < len(alphabet) - shift_amount ):
                    new_word += alphabet[index + shift_amount]
                else:
                    new_word += alphabet[shift_amount - (len(alphabet)- index)] 
            elif direction == "decode":
                if (index - shift_amount > 0 ):
                    new_word += alphabet[index - shift_amount]
                else:
                    new_word += alphabet[-(shift_amount - index)]

    print(f"The {direction}d text is : {new_word}")

replay = "yes"
while replay == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(direction, plain_text=text, shift_amount=shift)

    replay = input("Do You want to restart the cipher program ? :").lower()
    if replay != "yes":
        print("Goodbye")