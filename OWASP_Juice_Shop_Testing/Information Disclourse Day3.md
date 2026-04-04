# Web Security Analysis – Day 3
## Information Disclosure via Forced Browsing in OWASP Juice Shop

## Overview

This write-up documents **Day 3 of my Web Security Analysis series**, where I analyzed an **Information Disclosure vulnerability via Forced Browsing** while testing the **OWASP Juice Shop** application using **Burp Suite**.

Information Disclosure occurs when a web application unintentionally exposes sensitive data. Forced browsing is a technique where attackers manipulate URL paths to access hidden or restricted resources that are not properly secured.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Information Disclosure / Forced Browsing  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)
- **Web Browser Developer Tools**
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Exploring Application Functionality

While exploring the **About Us section** of the application, I identified a link pointing to a file located at:

```
/ftp/legal.md
```

This indicated the presence of a potentially accessible directory containing files.

---

## Step 2 – Manipulating the URL

To understand the directory structure, I modified the URL and accessed the base path:

```
/ftp/
```

This revealed multiple files within the directory, indicating that directory listing or direct access to files was enabled.

---

## Step 3 – Intercepting and Testing Requests

To further analyze the behavior, I intercepted the request using **Burp Suite Proxy** and sent it to **Burp Suite Repeater**.

I then experimented with different file paths within the `/ftp/` directory to check for accessible resources.

---

## Step 4 – Identifying the Vulnerability

By modifying the request to access another file:

```
/ftp/acquisitions.md
```

I was able to retrieve a **confidential internal document**.

This confirmed that sensitive files were accessible without proper authorization, demonstrating an **Information Disclosure vulnerability via Forced Browsing**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Access confidential company documents  
- Discover internal business information  
- Retrieve sensitive files not intended for public access  
- Perform further reconnaissance for advanced attacks  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Requests to hidden or uncommon directories  
- Repeated attempts to access different file paths  
- Unusual patterns in HTTP request logs  
- Suspicious directory enumeration behavior  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Disable **directory listing** on web servers  
- Enforce strict **access control mechanisms**  
- Store sensitive files outside publicly accessible directories  
- Implement proper **authorization checks** before serving files  

---

# Key Learning

This analysis demonstrates how simple URL manipulation can expose sensitive information if applications do not properly restrict access to internal directories and files.

Understanding directory structures and access controls is essential in identifying and preventing information disclosure vulnerabilities.

---

# Screenshots

## Accessing /ftp/ Directory
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Aboutus_ftp.png)


## Accessing Sensitive File (acquisitions.md)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Aboutus_confidentialfile.png)

