# Web Security Analysis – Day 11
## Broken Authentication via Weak Account Recovery Mechanism in OWASP Juice Shop

## Overview

This write-up documents **Day 11 of my Web Security Analysis series**, where I analyzed a **Broken Authentication vulnerability caused by weak account recovery mechanisms** in the **OWASP Juice Shop** application.

Account recovery mechanisms are a critical part of application security. If security questions rely on easily discoverable or publicly available information, attackers can exploit this weakness to reset passwords and gain unauthorized access to user accounts.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Broken Authentication / Weak Account Recovery  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Identifying Target Account

While exploring the application, I identified a user account named **bjoern** and focused on analyzing the password recovery functionality.

---

## Step 2 – Analyzing Account Recovery Mechanism

During the password reset process, I observed that the application relied on a security question:

"What is your favorite pet's name?"

This indicated that account recovery depended on knowledge-based authentication.

---

## Step 3 – Performing Reconnaissance

To find possible answers, I performed basic reconnaissance using publicly available information.

While exploring the **Photo Wall section**, I found references linked to the user’s social profile.

By analyzing publicly available posts, I gathered information that could be used to answer the security question.

---

## Step 4 – Exploiting the Vulnerability

Using the discovered information, I correctly answered the security question and successfully reset the account password.

This allowed me to gain unauthorized access to the user account.

---

## Step 5 – Identifying the Vulnerability

This demonstrates that the application relies on weak account recovery mechanisms that can be bypassed using publicly available information.

This confirms a **Broken Authentication vulnerability due to weak security questions**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Take over user accounts through password reset mechanisms  
- Exploit publicly available information for authentication bypass  
- Compromise user privacy and sensitive data  
- Perform further attacks using compromised accounts  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Unusual or repeated password reset attempts  
- Password resets followed by logins from new locations or devices  
- Suspicious account recovery patterns  
- Multiple failed or successful security question attempts  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Avoid using **knowledge-based security questions**  
- Implement **multi-factor authentication (MFA)** for account recovery  
- Limit password reset attempts and monitor anomalies  
- Use secure, time-bound reset tokens instead of static questions  

---

# Key Learning

This analysis highlights how weak account recovery mechanisms and reliance on publicly available information can lead to account takeover.

Even without exploiting technical vulnerabilities, attackers can gain unauthorized access by leveraging predictable or exposed user information.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_bjoern1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_bjoern2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_bjoern3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_bjoern4.png)
