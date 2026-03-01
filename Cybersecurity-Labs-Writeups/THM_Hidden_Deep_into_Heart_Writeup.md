# TryHackMe – Hidden Deep Into My Heart Writeup

### Platform
TryHackMe

### Room Name
Hidden Deep Into My Heart

---

### Overview

This room focused on web enumeration and access control weaknesses.  
The objective was to discover hidden files and gain unauthorized access to retrieve the flag.

The attack path involved:
- Directory brute forcing
- robots.txt discovery
- URL manipulation / IDOR
- Admin login using exposed credentials

---

### Tools Used

- Gobuster
- Wordlist: common.txt
- Web Browser
- Manual URL manipulation

---

### Step 1 – Directory Enumeration

I started by scanning the target web application using Gobuster.

Command used:

```bash
gobuster dir -u http://<target-ip>/ -w /usr/share/wordlists/dirb/common.txt
```
During enumeration, I discovered:

/robots.txt

Screenshot:

![Gobuster Scan](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_Interface.png)
![2](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_gobuster.png)
### Step 2 – Inspecting robots.txt

After accessing /robots.txt, I found:

A password

A hidden page reference (Cupid Secret Vault)

This indicated sensitive information disclosure through robots.txt.

Screenshot:

![Robots.txt](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_robot.png)
### Step 3 – Accessing Hidden Page

Using the path found in robots.txt, I navigated to the hidden page.

From there, I modified the URL by appending:

/administrator

This allowed access to the admin login page.

This technique is best described as:

URL Manipulation

Insecure Direct Object Reference (IDOR)

Broken Access Control

Screenshot:

![Admin Page](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_secretvalut.png)
### Step 4 – Admin Login

Username used:

admin

Password:

(Password found in robots.txt)

After logging in successfully, I gained access to the restricted section.

Screenshot:

![Admin Login Success](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_admin.png)
### Step 5 – Retrieving the Flag

Once authenticated as admin, I located and retrieved the flag.

Screenshot:

![Flag](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_DH_flag.png)
### Vulnerabilities Identified

Sensitive information exposed in robots.txt

Improper access control

URL manipulation allowing admin page access

Weak credential management

## Key Learnings

robots.txt should never contain sensitive data

Directory brute forcing is critical during reconnaissance

Broken Access Control is one of the most common web vulnerabilities

IDOR and URL manipulation can lead to privilege escalation

### Conclusion

This room demonstrated how simple enumeration and improper access control can lead to full administrative access. By combining directory brute forcing, information disclosure from robots.txt, and URL manipulation, it was possible to escalate privileges and retrieve the flag.

The challenge reinforced practical skills in:

Web enumeration

Access control testing

Authentication bypass techniques

Identifying insecure configurations

### Reference

Room completed on TryHackMe
Room Name: Hidden Deep Into My Heart
