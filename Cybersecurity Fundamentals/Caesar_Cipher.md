#  Caesar Cipher (Encryption & Decryption)
## Objective

The objective of this assignment is to implement a basic Caesar Cipher program in Python to encrypt and decrypt messages using a fixed shift value. This demonstrates how substitution ciphers work and how characters can be shifted using ASCII values and modular arithmetic.

### Code Explanation

A Python script was created with two functions:

encrypt(text, shift) – shifts each letter forward by the given number.

decrypt(text, shift) – shifts each letter backward by the same number.

Non-alphabet characters (spaces, symbols) remain unchanged.

A shift value of 4 was used for both encryption and decryption.

### Steps Performed
### Step 1 — Encrypting the Message

The plaintext message used was:

HELLO

Using a shift of 4, the encryption function converted it to:

LIPPS

### Step 2 — Decrypting the Ciphertext

The ciphertext used was:

Jg qh iwtg

Using the same shift value (4), the decryption function produced:

FC MD ESTC

### Code Used
```
def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            new_char = chr((ord(ch.upper()) - 65 + shift) % 26 + 65)
            result += new_char
        else:
            result += ch
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

message = "HELLO"
shift_value = 4
encrypted = encrypt(message, shift_value)

cipher_text = "Jg qh iwtg"
decrypted = decrypt(cipher_text, shift_value)

```

### Output

Original Message: HELLO
Encrypted Message: LIPPS

Cipher Text: Jg qh iwtg
Decrypted Message: FC MD ESTC

### Conclusion

This assignment demonstrated the basic working of the Caesar Cipher by implementing encryption and decryption using a fixed shift value. By shifting characters through the alphabet and applying modular arithmetic, it showed how classical substitution ciphers function. The results confirmed that text can be securely transformed and reversed using the same shift, providing a foundation for understanding more advanced cryptographic concepts.
