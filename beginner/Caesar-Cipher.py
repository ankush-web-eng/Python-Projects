alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to ecncrypt and 'decode' to decrypt\n")

def encode(text_letter, shift_amount):
    caeser = ""
    for i in text_letter:
        letter = alphabet.index(i)
        shift_letter = letter + shift_amount
        new_letter = alphabet[shift_letter]
        caeser += new_letter
    print(f"Your encoded Password is: {caeser}")


def decode(text_letter, shift_amount):
    caeser = ""
    for i in text_letter:
        letter = alphabet.index(i)
        shift_letter = letter - shift_amount
        new_letter = alphabet[shift_letter]
        caeser += new_letter
    print(f"Your decoded Password is {caeser}")


if direction == 'encode':
    text = input("type your Password:\n")
    shift = int(input("ENter the shift amount:\n"))
    encode(text, shift)
elif direction =='decode':
    text = input("type your Password:\n")
    shift = int(input("ENter the shift amount:\n"))
    decode(text,shift)
else:
    print("Enter correct Authentication Type!!")
