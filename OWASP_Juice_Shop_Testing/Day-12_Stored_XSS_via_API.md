# Web Security Analysis – Day 12
## Stored Cross-Site Scripting (XSS) via API in OWASP Juice Shop

## Overview

This write-up documents **Day 12 of my Web Security Analysis series**, where I analyzed a **Stored Cross-Site Scripting (XSS)** vulnerability triggered through an API in the **OWASP Juice Shop** application.

Stored XSS occurs when user-controlled input is accepted by the backend, stored in the database, and later rendered in the browser without proper sanitization or output encoding, leading to execution of malicious scripts.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Stored Cross-Site Scripting (XSS)  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Postman, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Postman** (API Testing)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Analyzing API Endpoints

After logging into the application, I analyzed network traffic using **browser developer tools** and identified user-related API endpoints such as:

```
/api/Users
```

These endpoints handle user-controlled data that is later rendered in the application.

---

## Step 2 – Sending Request via Postman

I used **Postman** to interact directly with the backend API and crafted a request to test how the application handles user-controlled input.

This approach bypasses frontend validation and directly tests server-side input handling.

---

## Step 3 – Injecting Malicious Payload

I modified the API request in Postman by injecting a script payload into one of the input fields and sent the request to the server.

The application accepted the input and stored it without proper validation or sanitization.

---

## Step 4 – Identifying the Vulnerability

Later, while accessing the **administrative section** and viewing user details, the stored data was rendered in the browser.

At this point, the injected script executed successfully, confirming a **Stored XSS vulnerability via API input**.

This indicates that the application fails to sanitize input at the backend and does not properly encode output before rendering.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Execute malicious scripts in other users’ browsers  
- Steal session tokens or sensitive information  
- Perform actions on behalf of authenticated users  
- Deface or manipulate application content  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Suspicious payloads in API request bodies  
- Malicious input stored in application data  
- Script-like content appearing in user profiles or data fields  
- Alerts triggered by Web Application Firewalls (WAF)  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Validate and sanitize all inputs on the **server side**  
- Implement proper **output encoding** before rendering data  
- Apply strict **input validation** for API endpoints  
- Use **Content Security Policy (CSP)** to restrict script execution  

---

# Key Learning

This analysis highlights that APIs are a critical attack surface in modern web applications.

By using Postman to bypass frontend validation, it was possible to directly test backend behavior and identify improper input handling, leading to a **Stored XSS vulnerability**.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_clientxss1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_clientxss2.png)
