# Caesar Cipher
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
# Create a biggre list to avoide errors
alp = alphabet + alphabet


def caesar(text, shift, dir):
    cipher_text = ''
    # This condition will treger the decode
    if dir == 'decode':
        shift *= -1
    for i in text:
        if i in alp:
            pos = alp.index(i) + shift
            cipher_text += alp[pos]
        else:
            cipher_text += i
    print(f"The {dir}d text is {cipher_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text_new = input('Type your message:\n').lower()
    shift_amount = int(input("Type the shift number:\n"))

    # Control the shift size so it fits in alp
    shift_amount = shift_amount % 26

    caesar(text=text_new, shift=shift_amount, dir=direction)

    # Check if the user wants to keep going
    result = input(
            "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
