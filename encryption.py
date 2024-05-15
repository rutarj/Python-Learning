# - The Python code implements a Caesar cipher, a technique for encryption and decryption.
# - The alphabet list is initialized, containing lowercase letters duplicated for boundary handling.
# - User inputs include the cipher direction (encoding or decoding), the text to process, and the shift amount.
# - The core `caesar()` function handles encryption and decryption.
# - It iterates over each letter, calculates the new position after shifting, and appends the result.
# - Shift direction adjusts based on the user's choice, with the final result printed.

# - In the function call, `caesar()` is invoked with user-provided inputs.
# - Depending on the direction, the function encrypts or decrypts the text.
# - Encryption shifts each letter forward by the specified amount.
# - Decryption reverses the shift by moving letters backward.
# - The modulo operator ensures shifts wrap around the alphabet's bounds.
# - The code offers a simple yet effective demonstration of the Caesar cipher technique.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
