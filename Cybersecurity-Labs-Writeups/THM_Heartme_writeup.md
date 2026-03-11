# TryHackMe Write-up – HeartMe Room

## Overview

This write-up documents my approach to solving the **HeartMe room on TryHackMe**.  
The objective of the challenge was to analyze the web application, identify security weaknesses, and retrieve the hidden **Valenflag**.

During this room, I explored the website, performed directory enumeration, inspected cookies, and exploited a **JWT (JSON Web Token) misconfiguration** to gain **admin privileges** and purchase a staff-only item containing the flag.

---

## Tools Used

- Browser Developer Tools
- Gobuster
- JWT.io
- Burp Suite (optional)

---

## Step 1 – Initial Website Exploration

I started by visiting the target website and exploring the available pages and functionality.

The application appeared to be a **Valentine-themed shopping website** where users could purchase items using **CPE credits**.

During this stage I:
- Navigated through different pages
- Checked for hidden parameters
- Observed how authentication worked

---

## Step 2 – Directory Enumeration

Next, I attempted to discover hidden directories using **Gobuster**.

```bash
gobuster dir -u http://<target-ip> -w /usr/share/wordlists/dirb/common.txt
```
However, the scan did not reveal any useful hidden directories or endpoints.

Since enumeration did not produce results, I decided to inspect the application further.

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_Heartme_gobuster.png)

### Step 3 – Inspecting Cookies

Using Browser Developer Tools, I inspected the Application → Cookies section.

Here I discovered a JWT token stored in the cookie which appeared to contain user information.
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_Heartme_cookiejwt.png)

### Step 4 – Decoding the JWT Token

I copied the JWT token and pasted it into JWT.io to decode the payload.

The token contained information such as:
```
{
  "email": "user@test.com",
  "role": "user",
  "cpe_credits": 10
}
```
This indicated that the application used JWT tokens to control user roles and credits.


### Step 5 – Modifying the JWT Token

Since the token payload could be modified, I attempted privilege escalation.

I modified the values to:
```
{
  "email": "test@test.com",
  "role": "admin",
  "cpe_credits": 999
}
```
After modifying the payload:

I generated a new token using JWT.io

Copied the modified JWT

Replaced the original cookie value in the browser
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_Heartme_jwt.png)

### Step 6 – Accessing the Admin Dashboard

After replacing the cookie value with the modified token, I refreshed the page and accessed the admin dashboard via URL manipulation.

Example:

/admin

This successfully granted access to the admin panel.

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_Heartme_admin.png)

### Step 7 – Purchasing the Hidden Valenflag

Inside the admin dashboard, I discovered a special item available only for staff called:

Valenflag

Since my role was now admin and I had 999 CPE credits, I was able to purchase this item.

After purchasing the Valenflag, the final flag was revealed.

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_Heartme_valenflag.png)

### Vulnerabilities Identified
1. Insecure JWT Implementation

The application allowed modification of the JWT payload without proper verification.

2. Privilege Escalation

By changing the role field to admin, I gained access to restricted functionality.

3. Trusting Client-Side Data

The application relied on user-controlled JWT values such as role and credits.

### Security Insights

How JWT tokens work in authentication systems

Risks of improper JWT validation

How attackers exploit JWT privilege escalation

Importance of server-side validation for authorization


### Conclusion

This room demonstrated how insecure JWT implementations can lead to privilege escalation and unauthorized access. By modifying the JWT token stored in cookies, I was able to gain admin privileges, access the admin dashboard, and purchase the hidden Valenflag to obtain the final flag.

### Reference
Room: HeartMe
Platform: TryHackMe
Category: Web Security / JWT Exploitation
