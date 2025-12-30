# BTLO – Secrets Challenge (JWT Analysis & Cracking)

## Platform
Blue Team Labs Online (BTLO)

## Challenge Name
Secrets

## Difficulty
Beginner–Intermediate

---

## Objective
The objective of this challenge was to analyze a provided token, identify its structure, extract hidden information, crack the JWT secret, and generate a new valid token with lower privileges.

This challenge focuses on:
- JWT structure analysis
- Base64 decoding
- Secret key cracking
- Token manipulation and re-signing

---

## Tools Used
- Base64 Decoder (Online)
- Hashcat
- jwt.io
- Kali Linux

---

## Provided Token
```text
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOnRydWV9.jbkZHll_W17BOALT95JQ17glHBj9nY-oWhT1uiahtv8
```
## Step 1 — Identify the Token Type
The token was decoded using a Base64 decoder.

From the decoded header:
```
json
 
{
  "typ": "JWT",
  "alg": "HS256"
}
```
Answer
JWT

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/blueteam_Secret1.png)


## Step 2 — Identify the Token Structure
JWT tokens follow a standard three-part structure separated by dots:

``` 
Header.Payload.Signature
Header: Algorithm and token type
```
Payload: Claims (data)

Signature: Integrity verification

 Answer
Header.Payload.Signature

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/blueteam_Secret2.png)

## Step 3 — Identify the Hint from the Token
From the decoded payload:
```
json
 
{
  "flag": "BTL{_4_Eyes}",
  "iat": 90000000,
  "name": "GreatExp",
  "admin": true
}
```
Answer
_4_Eyes


## Step 4 — Crack the JWT Secret
Since the token used HS256 (HMAC-SHA256), the signature depended on a shared secret.

Hashcat Command Used
```
bash
 
hashcat -m 16500 token.txt -a 3 ?a?a?a?a?a?a?a?a?a?a?a?a?a?a?a --increment
```
Explanation
-m 16500: JWT (HS256) hash mode

-a 3: Mask attack

?a: All printable characters

--increment: Increment secret length automatically

The secret key was successfully cracked.

Answer
bT!0

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/blueteam_Secret3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/blueteam_Secret4.png)

## Step 5 — Generate a New Low-Privilege Token
Using jwt.io, the following steps were performed:

Pasted the original token

Entered the cracked secret key: bT!0

Modified the payload by changing "admin": true to "admin": false

Generated a new valid signature

New Low-Privilege JWT
text
``` 
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOmZhbHNlfQ.nMXNFvttCvtDcpswOQA8u_LpURwv6ZrCJ-ftIXegtX4
```
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/blueteam_Secret6jwttoken.png)

## Summary of Findings
The token was identified as a JWT using HS256

Sensitive data was exposed inside the payload

A weak secret key allowed brute-force cracking

Token privileges could be modified after re-signing

Demonstrates risks of insecure JWT implementations

## Key Learnings
Understanding JWT internals is critical for security analysis

Weak JWT secrets can lead to privilege manipulation

HS256 tokens must be protected with strong secrets

Proper validation and rotation of secrets is essential



## Conclusion
This challenge demonstrated how insecure JWT implementations can be exploited to manipulate privileges. By decoding, cracking, and re-signing the token, it was possible to generate a valid low-privilege JWT. The exercise highlights the importance of strong secret management and secure token handling in real-world applications.

## Reference
Challenge completed on Blue Team Labs Online (BTLO)
Challenge Name: Secrets
