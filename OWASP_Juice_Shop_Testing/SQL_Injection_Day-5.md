# Web Security Analysis – Day 5
## SQL Injection in OWASP Juice Shop

## Overview

This write-up documents **Day 5 of my Web Security Analysis series**, where I analyzed a **SQL Injection vulnerability** while testing the **OWASP Juice Shop** application.

SQL Injection occurs when user input is not properly validated or sanitized before being included in database queries. This allows attackers to manipulate queries and potentially access unauthorized data from the database.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** SQL Injection  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)
- **Web Browser Developer Tools**
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Testing the Login Functionality

While interacting with the **login functionality**, I tested how the application handled user input in the authentication fields.

The objective was to check whether the application properly validates and processes user credentials.

---

## Step 2 – Injecting SQL Payloads

By modifying the input fields and injecting SQL payloads, I tested whether the application was vulnerable to SQL Injection.

These payloads were designed to manipulate the backend database query used for authentication.

---

## Step 3 – Bypassing Authentication

After submitting the crafted input, I was able to bypass the normal authentication mechanism and successfully log in as the **administrator**.

This indicates that the application did not properly sanitize user input before executing database queries.

---

## Step 4 – Accessing Sensitive Data

After gaining administrative access, I navigated to the **administrator section** of the application.

This exposed sensitive information, including:

- Admin users' email addresses  
- User feedback data stored in the system  

This confirms that the SQL Injection vulnerability allowed unauthorized access to critical application data.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Bypass authentication mechanisms  
- Access sensitive user information stored in databases  
- Extract confidential data such as emails or credentials  
- Modify or delete critical application data  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Suspicious input patterns in login requests  
- SQL syntax appearing in user inputs  
- Abnormal authentication behavior in logs  
- Repeated login attempts with manipulated parameters  

---

# Mitigation Strategies

To prevent SQL Injection vulnerabilities, developers should implement:

- Use **parameterized queries** or prepared statements  
- Proper **input validation and sanitization**  
- Apply **least privilege access** to database accounts  
- Deploy **Web Application Firewalls (WAF)** to detect malicious inputs  

---

# Key Learning

This analysis highlights how improper handling of user input in database queries can lead to serious security risks.

SQL Injection remains one of the most critical vulnerabilities, as it allows attackers to bypass authentication and access sensitive application data.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Login.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Login1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Login2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_adminstration.png)
