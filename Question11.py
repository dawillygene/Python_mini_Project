def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            new_char = char
        encrypted_text += new_char

    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift) 


plaintext = input("Enter the text to encrypt: ")
shift_value = int(input("Enter shift value: "))


ciphertext = encrypt(plaintext, shift_value)
decrypted_text = decrypt(ciphertext, shift_value)


print("\nEncrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
