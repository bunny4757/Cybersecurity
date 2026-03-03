# TryHackMe – Signed Messages Writeup

## Platform
TryHackMe

## Room Name
Signed Messages

---

## Overview

This room focused on digital signatures and how improper key management can lead to privilege escalation.

The objective was to analyze the web application, regenerate the admin private key, and use it to successfully verify a signed message as the administrator to retrieve the flag.

---

## Tools Used

- Gobuster
- Wordlist: common.txt
- Python
- Web Browser

---

### Step 1 – Initial Enumeration

After analyzing the website manually, no obvious vulnerabilities were found.

To discover hidden resources, I performed directory brute forcing using Gobuster:

```bash
gobuster dir -u http://<target-ip>/ -w /usr/share/wordlists/dirb/common.txt
```
During enumeration, I discovered:

/debug

Screenshot:

![Gobuster Scan](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_Interface.png)
![2](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_fuzz.png)
### Step 2 – Analyzing the Debug Page

After accessing /debug, it revealed sensitive information explaining how the admin private key was generated.

The page contained enough logic details to allow replication of the admin key generation process.

This was a critical information disclosure vulnerability.

Screenshot:

![Debug Page](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_Debug.png)
### Step 3 – Regenerating the Admin Private Key

Using the information from the debug page, I wrote a Python script to replicate the private key generation logic exactly as implemented by the application.

The script successfully regenerated the admin private key.
```
Python Script

import hashlib
from sympy import nextprime
from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256
 
# crypto-nerd: what this file does (dumbed down)
# - recreate the server's tiny RSA private key from a predictable "seed"
# - use that private key to produce a PSS+SHA256 signature for a message
# - prints the signature in hex so you can paste it into the victim's verify endpoint
# (yes, this is the tiny CTF attack pattern: predictable seed -> rebuild key -> sign)
 
TARGET_USER = "admin"
# crypto-nerd: the exact message the server verifies — must match byte-for-byte
TARGET_MESSAGE = "Welcome to LoveNote! Send encrypted love messages this Valentine's Day. Your communications are secured with industry-standard RSA-2048 digital signatures."
 
 
def generate_admin_key():
    # crypto-nerd: build the same deterministic seed the server used
    seed_str = f"{TARGET_USER}_lovenote_2026_valentine"
    seed_bytes = seed_str.encode('utf-8')
 
    # crypto-nerd: hash the seed to produce a large integer, then pick the next prime
    # this mimics a naive key-derivation the server used (not secure)
    sha256_p = hashlib.sha256(seed_bytes).hexdigest()
    p = nextprime(int(sha256_p, 16))
 
    # crypto-nerd: tweak the seed and derive q the same way (so p and q are predictable)
    sha256_q = hashlib.sha256(seed_bytes + b"pki").hexdigest()
    q = nextprime(int(sha256_q, 16))
 
    # crypto-nerd: construct RSA components. e is the public exponent (usual choice 65537)
    n = p * q
    e = 65537
    phi = (p - 1) * (q - 1)
 
    # crypto-nerd: modular inverse of e modulo phi -> private exponent d
    d = pow(e, -1, phi)
 
    # crypto-nerd: return a Crypto.PublicKey.RSA object constructed from (n, e, d)
    return RSA.construct((n, e, d))
 
 
def forge_signature(key, message):
    # crypto-nerd: hash the message with SHA-256 — that's what PSS will sign
    h = SHA256.new(message.encode('utf-8'))
 
    # crypto-nerd: we must compute maximum salt size for PSS given the key length
    # modBits = number of bits in the modulus n
    modBits = key.size_in_bits()
 
    # emLen = ceil((modBits - 1)/8)  -> length of the encoded message in bytes
    emLen = (modBits - 1 + 7) // 8
 
    # maxSalt = emLen - digestLen - 2  (digestLen is 32 for SHA-256)
    maxSalt = emLen - h.digest_size - 2
 
    if maxSalt < 0:
        raise ValueError("Key is too small even for 0 salt!")
 
    # crypto-nerd: create a PSS signer forcing the salt length to the computed maximum
    signer = pss.new(key, salt_bytes=maxSalt)
    signature = signer.sign(h)
 
    # crypto-nerd: output hex so it's easy to paste into web forms
    return signature.hex()
 
 
if __name__ == '__main__':
    try:
        admin_key = generate_admin_key()
        signature = forge_signature(admin_key, TARGET_MESSAGE)
 
        print("\n" + "="*60)
        print(" >>> FINAL ADMIN SIGNATURE <<< ")
        print("="*60)
        print(signature)
        print("="*60)
        print("1. Go to Verify Page.")
        print("2. User: admin")
        print("3. Paste the signature above.")
 
    except Exception as e:
        print(f"[!] Error: {e}")
```

### Step 4 – Verifying as Admin

The application had a verify page where:

A user could be selected (e.g., admin)

A message could be submitted

A private key could be provided for verification

I selected:

User: admin

Then:

Entered a message

Provided the regenerated admin private key

After submitting the form, the verification succeeded.

Screenshot:

![Verify Page](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_signature.png)
![4](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_message.png)
### Step 5 – Retrieving the Flag

Upon successful verification as admin, the application revealed the flag.

Screenshot:

![Flag](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_SM_flag.png)
## Vulnerabilities Identified

Sensitive debug endpoint exposed

Predictable private key generation

Improper key management

Information disclosure leading to privilege escalation

## Key Learnings

Debug pages should never be exposed in production

Private keys must never be predictable

Cryptographic implementations must use secure randomness

Information disclosure can completely break authentication systems

Directory brute forcing is critical during enumeration

## Conclusion

This room demonstrated how weak cryptographic implementation and exposed debugging information can completely compromise a system.

By discovering the debug endpoint, replicating the admin private key generation logic, and using it on the verification page, it was possible to escalate privileges and retrieve the flag.

This challenge strengthened practical skills in:

Web enumeration

Cryptographic analysis

Python scripting

Authentication bypass techniques

## Reference

Room completed on TryHackMe
Room Name: Signed Messages
