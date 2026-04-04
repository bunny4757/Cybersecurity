# Web Security Analysis – Day 6
## Insecure Direct Object Reference (IDOR) in OWASP Juice Shop

## Overview

This write-up documents **Day 6 of my Web Security Analysis series**, where I analyzed an **Insecure Direct Object Reference (IDOR)** vulnerability while testing the **OWASP Juice Shop** application.

IDOR occurs when an application exposes internal object identifiers (such as user IDs, order IDs, or basket IDs) without properly verifying whether the authenticated user is authorized to access that resource.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Insecure Direct Object Reference (IDOR)  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)
- **Web Browser Developer Tools**
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Interacting with Basket Functionality

After logging into the application, I added items to my basket to generate activity related to user-specific resources.

This allowed me to observe how the application handles basket-related requests.

---

## Step 2 – Intercepting the Request

I intercepted the request using **Burp Suite Proxy** and sent it to **Burp Suite Repeater** for further analysis.

While reviewing the request, I noticed the following endpoint:

```
/rest/basket/33
```

The numeric value appeared to represent a **basket ID**.

---

## Step 3 – Manipulating the Object Identifier

To test whether proper authorization checks were implemented, I modified the basket ID in the request:

```
/rest/basket/4
```

The modified request was then resent to the server.

---

## Step 4 – Identifying the Vulnerability

After sending the modified request, the application responded with basket details belonging to another user.

This confirms that the application does not properly verify whether the requesting user is authorized to access the specified resource.

This behavior demonstrates an **Insecure Direct Object Reference (IDOR)** vulnerability.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Access other users’ personal or account information  
- View or manipulate other users’ orders or transactions  
- Retrieve sensitive application data  
- Enumerate object IDs to expand the attack scope  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Repeated requests with modified object identifiers  
- Unusual access patterns to sequential resource IDs  
- Suspicious enumeration attempts in application logs  
- API requests accessing resources belonging to different users  

---

# Mitigation Strategies

To prevent IDOR vulnerabilities, developers should implement:

- Proper **authorization checks** on every request  
- Ensure users can only access resources they own  
- Avoid exposing direct object identifiers where possible  
- Use indirect references or enforce server-side access control validation  

---

# Key Learning

This analysis highlights how improper authorization checks on object identifiers can allow attackers to access data belonging to other users.

Ensuring proper access control is critical to maintaining user privacy and application security.

---

# Screenshots
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_basetchange.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_basetchange1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_basetchange2.png)
