#Caesar cipher program that encrypts and decyrpts a message using a shift value provided by the user
print("==============================")
print("       CAESAR CIPHER")
print("==============================")
# Get message and shift value from user
message = input("Enter a test message:")
shift = int(input ("Enter shift value:"))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Encrypt the message
encrypted_message = ""

for char in message.upper():
    if char in alphabet:
        position = alphabet.index(char)

        new_position = (position + shift) % 26

        encrypted_message += alphabet[new_position]
    else:
        encrypted_message += char

print("\nOriginal message:", message)
print("Shift value:", shift)
print("Encrypted message:", encrypted_message)
# Decrypt the encrypted message
decrypted_message = ""

for char in encrypted_message:
    if char in alphabet:
        position = alphabet.index(char)

        new_position = (position - shift) % 26

        decrypted_message += alphabet[new_position]
    else:
        decrypted_message += char

print("Decrypted message:", decrypted_message)