
def encrypt(plain_text, shift_amount):
    cipher_test=""
    for letter in plain_text:
         position=alphabet.index(letter)
         newposition=position+shift_amount
         newletter=alphabet[newposition]
         cipher_test+=newletter
    print(cipher_test)
    return cipher_test

def decrypt(plain_test,shift_amount):
    decrpyt_word=""
    for letter in plain_test:
        position=alphabet.index(letter)
        newposition=position-shift_amount
        newletter=alphabet[newposition]
        decrpyt_word+=newletter
    print(decrpyt_word)

while True:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input(f"Type your message to {direction}:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:print("invaild enter encode or decode")


