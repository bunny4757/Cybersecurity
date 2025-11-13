# Caesar Cipher (Encryption & Decryption)

## 📘 Overview
This assignment demonstrates the use of the **Caesar Cipher**, one of the earliest and simplest encryption techniques in cryptography.  
It focuses on understanding how substitution ciphers work by shifting letters in the alphabet by a fixed number of positions.

---

## 💡 Concept
In a Caesar Cipher, each letter in the plaintext is replaced by another letter that is a certain number of positions down the alphabet.

For example, with a shift of 4:
Plain: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher: E F G H I J K L M N O P Q R S T U V W X Y Z A B C D

Thus,  
**HELLO → LIPPS**

---

## 🎯 Objective
- Encrypt the message **"HELLO"** using a Caesar Cipher with a shift of **4**.  
- Decrypt the ciphertext **"Jg qh iwtg"** using the reverse shift.

---

## 🧪 Expected Output
Original Message: HELLO
Encrypted Message: LIPPS

Cipher Text: Jg qh iwtg
Decrypted Message: FC MD ESTC

---

## 📚 Key Learning Points
- Understanding basic **encryption and decryption** mechanisms  
- Working with **character encoding (ASCII)**  
- Learning how **modular arithmetic** enables letter shifting and wrap-around (Z → A)  
- Introduction to **substitution ciphers** in cybersecurity
