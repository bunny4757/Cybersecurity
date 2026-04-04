# Web Security Analysis – Day 9
## API-Based Cross-Site Scripting (XSS) in OWASP Juice Shop

## Overview

This write-up documents **Day 9 of my Web Security Analysis series**, where I analyzed an **API-based Cross-Site Scripting (XSS)** vulnerability caused by improper input handling in the **OWASP Juice Shop** application.

Cross-Site Scripting (XSS) is not limited to web forms. It can also occur through APIs if user input is not properly validated or sanitized before being stored and rendered in the application.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Cross-Site Scripting (XSS)  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Analyzing API Requests

After logging into the application, I used **browser developer tools** to analyze network traffic.

During this process, I identified API requests containing a **Bearer Authorization token**, indicating authenticated communication with backend services.

---

## Step 2 – Testing API Input Handling

Using the captured token, I analyzed how the backend API handled user-controlled input.

I crafted a request targeting a **product-related API endpoint** and modified the request body to include controlled input.

---

## Step 3 – Injecting Malicious Payload

I injected a script payload into the API request and submitted it to the server.

The application accepted the input and stored it without proper validation or sanitization.

---

## Step 4 – Identifying the Vulnerability

After refreshing the application, the newly created product appeared in the product list with the injected script payload.

This confirms that the application is vulnerable to **Stored XSS via API input**, as it fails to sanitize user-supplied data received through backend services.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Inject malicious scripts into application content  
- Execute scripts in other users’ browsers  
- Steal session tokens or sensitive data  
- Deface or manipulate application content  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Suspicious payloads in API request bodies  
- Unusual API usage patterns involving authorization tokens  
- Script-like input appearing in stored data  
- Alerts triggered by Web Application Firewalls (WAF)  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Validate and sanitize all user inputs on the **server side**  
- Implement **output encoding** before rendering data  
- Apply strict **input validation** for API endpoints  
- Use security headers such as **Content Security Policy (CSP)**  

---

# Key Learning

This analysis highlights that APIs are a critical attack surface in modern web applications.

Improper input validation in backend services can lead to **stored XSS vulnerabilities**, which can impact multiple users and compromise application security.

---

# Screenshots

## API Request Interception with Bearer Token
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_api_xss.png)

## Modified API Request with Payload
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_api_xss1.png)

## Stored XSS Reflected in Application
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_api_xss2.png)
