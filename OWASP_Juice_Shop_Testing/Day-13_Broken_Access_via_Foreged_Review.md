# Web Security Analysis – Day 13
## Broken Access Control via Review Forgery in OWASP Juice Shop

## Overview

This write-up documents **Day 13 of my Web Security Analysis series**, where I analyzed a **Broken Access Control vulnerability** that allowed forging product reviews in the **OWASP Juice Shop** application.

Broken Access Control occurs when an application fails to properly enforce restrictions on user actions, allowing attackers to manipulate data or perform actions on behalf of other users.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Broken Access Control  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Submitting a Product Review

While exploring the **product review functionality**, I submitted a review using my account to understand how the application processes review data.

---

## Step 2 – Intercepting the Request

I intercepted the review submission request using **Burp Suite Proxy** and sent it to **Burp Suite Repeater** for further analysis.

During this step, I examined how the application identifies the author of the review.

---

## Step 3 – Modifying Author Information

While analyzing the request, I identified a field representing the **review author**.

To test access control, I modified this field to impersonate another user and resent the request.

---

## Step 4 – Identifying the Vulnerability

After resending the modified request, the application accepted the input and stored the review under a different user's identity.

This confirms that the application does not properly validate whether the authenticated user is authorized to perform actions on behalf of another user.

This behavior demonstrates a **Broken Access Control vulnerability leading to review forgery**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Impersonate other users while submitting reviews  
- Manipulate product ratings and feedback  
- Damage trust and credibility of the platform  
- Perform reputation-based attacks  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Mismatched user identities in request data  
- Unusual patterns in review submissions  
- Requests containing manipulated author fields  
- Logs showing actions performed across multiple user identities  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Enforce strict **server-side authorization checks**  
- Derive user identity from **session/token**, not client input  
- Avoid trusting **client-controlled fields** for sensitive actions  
- Implement proper validation for all user-generated content  

---

# Key Learning

This analysis highlights how improper access control can allow attackers to forge actions on behalf of other users.

Ensuring proper authorization and avoiding reliance on client-controlled data is essential to maintain integrity and trust within applications.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_forgedreview1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_forgedreview2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_forgedreview3.png)

