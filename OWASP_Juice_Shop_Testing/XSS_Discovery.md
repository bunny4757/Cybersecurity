# Web Security Analysis – Day 1
## Cross-Site Scripting (XSS) in OWASP Juice Shop

## Overview

This write-up documents **Day 1 of my Web Security Analysis series**, where I analyzed a **Cross-Site Scripting (XSS)** vulnerability while testing the **OWASP Juice Shop** application using **Burp Suite**.

Cross-Site Scripting (XSS) occurs when a web application fails to properly validate or sanitize user input, allowing attackers to inject malicious scripts that execute in the victim’s browser.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Cross-Site Scripting (XSS)  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & HTTP History)
- **Web Browser Developer Tools**
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Intercepting Traffic

First, I configured **Burp Suite Proxy** to intercept the browser traffic.

This allowed me to observe how the application processes user inputs and communicates with the backend.

By analyzing the requests and responses, I was able to monitor how search parameters were being handled.

---

## Step 2 – Testing the Search Functionality

While testing the **search functionality** in OWASP Juice Shop, I experimented with different input values.

The goal was to observe how the application processes user input and whether the input is properly validated or sanitized.

---

## Step 3 – Identifying the Vulnerability

By modifying the input and analyzing the request/response behavior through **Burp Suite**, I discovered that the application reflected user input directly in the browser without proper sanitization.

This allowed injected script content to execute in the browser, confirming the presence of a **Reflected XSS vulnerability**.

---

# Potential Impact

If exploited in a real-world application, attackers could potentially:

- Steal **session cookies**
- Perform actions on behalf of authenticated users
- Redirect users to malicious websites
- Execute arbitrary scripts in the victim's browser

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Suspicious script patterns in **HTTP requests**
- Repeated injection attempts in **input parameters**
- **Web Application Firewall (WAF)** alerts
- Abnormal request payloads in **web logs**

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Proper **input validation**
- **Output encoding**
- Implementation of **Content Security Policy (CSP)**
- Secure handling of **user-supplied input**

---

# Key Learning

This exercise highlighted how even simple input fields such as **search bars** can become potential attack vectors if user input is not properly validated or sanitized.

Understanding how user inputs are processed is critical in identifying and preventing web vulnerabilities.

---

# Screenshots

## Burp Suite Request Interception
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Xss_2.png)

## XSS Payload Execution
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_XSS_Injection.png)

## Browser Response Showing Script Execution
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_xss_sucess.png)
