# RSA Key Pair Generation using OpenSSL
## Objective

The purpose of this assignment is to generate an RSA private key and derive the corresponding public key using OpenSSL. This includes verifying OpenSSL installation, generating encrypted key files, and viewing them in PEM format.

### Step 1 — Verify OpenSSL Installation

Open your terminal (Linux, Mac, or Windows Git Bash) and run:

``
openssl version
``

If OpenSSL is installed, it will return a version number such as:

OpenSSL 3.x.x

### Step 2 — Generate the RSA Private Key

Run the following command:
```
openssl genpkey -algorithm RSA -out private_key.pem -aes256
```

This command:

Generates a 2048-bit (default) RSA private key

Encrypts it using AES-256

Saves it to private_key.pem

Prompts you to set a password (you can use: 1234)

### Step 3 — View the Private Key (PEM Format)

Use:
```
cat private_key.pem
```

Sample output format:

-----BEGIN ENCRYPTED PRIVATE KEY-----
(base64 encoded content)
-----END ENCRYPTED PRIVATE KEY-----

### Step 4 — Generate the Public Key

Extract the public key from the private key:
```
openssl rsa -pubout -in private_key.pem -out public_key.pem
```
You will be asked for the password you set earlier (1234).

### Step 5 — View the Public Key (PEM Format)

Run:
```
cat public_key.pem
```

You will see output similar to:

-----BEGIN PUBLIC KEY-----
(base64 encoded content)
-----END PUBLIC KEY-----

### Screenshots:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity%20Fundamentals/Images/rsa%20private%20key.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity%20Fundamentals/Images/rsa%20public%20key.png)

### Conclusion

This assignment demonstrated how to:

Verify OpenSSL installation

Generate an RSA private key with AES-256 encryption

Extract the corresponding public key

Display both keys in PEM format
