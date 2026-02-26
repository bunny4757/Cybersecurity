# TryHackMe – Valentine (Valen Find) Writeup

## Platform
TryHackMe

## Room Name
Valentine (Valen Find)

## Difficulty
Medium / Web Exploitation

---

## Overview

This room focused on web application analysis and exploitation.  
The objective was to investigate a Valentine's-themed website, identify vulnerabilities, and gain access to a restricted database to retrieve the flag.

The attack chain involved:
- Website enumeration
- Source code inspection
- Local File Inclusion (LFI)
- API manipulation
- Credential discovery
- Privilege escalation via exposed API key

---

## Initial Recon

After accessing the web application, I:

1. Created a user account
2. Explored user profiles
3. Sent valentines between users
4. Interacted with various features to understand application behavior

While navigating the site, I inspected the page source and discovered a commented hint indicating a potential vulnerability.

Screenshot:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_2.png)

---

## Vulnerability Discovery – Local File Inclusion (LFI)

The comment in the source code suggested improper input handling in the API fetch mechanism.

By manipulating the API request parameters, I was able to exploit a **Local File Inclusion (LFI)** vulnerability.

This allowed me to access internal files on the server.

Example concept:

/api/fetch?file=../../app.py


Screenshot:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_5_Page_Source.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_4_LF_S.png)

---

## Accessing Sensitive Files

Using LFI, I accessed the backend file:


app.py


Inside the file, I discovered sensitive information including:

- Admin API endpoint
- Admin API key/token
- Reference to the internal database: `cupid.db`

Screenshot:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_6_Path.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_7_DB.png)

---

## Privilege Escalation via API Key

After extracting the admin API key from `app.py`, I used it to authenticate against the admin API endpoint.

By including the valid admin token in the request headers, I gained elevated access to the restricted API.

Example concept:

Authorization: Bearer <admin_api_key>


Screenshot:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_9_approute.png)

---

## Database Access – Cupid DB

With admin privileges, I accessed the internal database:


cupid.db


From there, I retrieved the hidden flag.

Screenshot:
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_VF_8_Flag.png)

---

## Key Vulnerabilities Identified

- Source code information disclosure
- Local File Inclusion (LFI)
- Hardcoded admin API key
- Improper access control
- Sensitive database exposure

---

## Key Learnings

- Always inspect page source for hidden hints
- LFI can expose critical backend files
- Hardcoded secrets in source code are dangerous
- APIs must enforce proper authentication and access control
- Sensitive files like `.db` and `.py` should never be publicly accessible

---

## Conclusion

This room demonstrated how small misconfigurations in web applications can lead to full compromise. By combining source code analysis, LFI exploitation, and API manipulation, it was possible to escalate privileges and access a protected database.

The lab reinforced practical skills in:
- Web enumeration
- LFI exploitation
- API security analysis
- Backend code inspection
- Privilege escalation techniques

---

## Reference
Room completed on TryHackMe  
Room Name: Valentine (Valen Find)
