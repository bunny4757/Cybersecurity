# Simple Caesar Cipher Program
# Assignment 1 - Cyber Security Fundamentals

def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():  # check if character is a letter
            new_char = chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
            result += new_char
        else:
            result += ch  # keep spaces or symbols unchanged
    return result

def decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            new_char = chr((ord(ch.upper()) - 65 - shift) % 26 + 65)
            result += new_char
        else:
            result += ch
    return result

# --- Encrypt the message "HELLO" with shift of 4 ---
message = "HELLO"
shift_value = 4
encrypted = encrypt(message, shift_value)
print("Original Message:", message)
print("Encrypted Message:", encrypted)

# --- Decrypt the message "Jg qh iwtg" ---
cipher_text = "Jg qh iwtg"
decrypted = decrypt(cipher_text, shift_value)
print("\nCipher Text:", cipher_text)
print("Decrypted Message:", decrypted)

