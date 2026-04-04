# Web Security Analysis – Day 8
## Broken Access Control in OWASP Juice Shop

## Overview

This write-up documents **Day 8 of my Web Security Analysis series**, where I analyzed a **Broken Access Control vulnerability** that allowed manipulation of user-associated data in the **OWASP Juice Shop** application.

Broken Access Control occurs when an application fails to properly enforce restrictions on what authenticated users are allowed to do, allowing attackers to interact with or modify resources belonging to other users.

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

## Step 1 – Testing Customer Feedback Functionality

While exploring the **Customer Feedback functionality**, I submitted a feedback entry to observe how the application processes user-generated data.

---

## Step 2 – Intercepting the Request

I intercepted the feedback submission request using **Burp Suite Proxy** and forwarded it to **Burp Suite Repeater** for further analysis.

During this step, I examined how user-related data was included in the request.

---

## Step 3 – Modifying User Identifier

While analyzing the request, I identified a **user identifier** associated with the feedback submission.

To test authorization controls, I modified this identifier and resent the request to the server.

---

## Step 4 – Identifying the Vulnerability

After modifying the user ID, the application accepted the request and stored the feedback under a different user's account.

This confirms that the application does not properly validate whether the authenticated user is authorized to perform actions on behalf of another user.

This behavior demonstrates a **Broken Access Control vulnerability**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Submit or manipulate data on behalf of other users  
- Tamper with user-generated content  
- Impersonate other users within the system  
- Compromise data integrity and trust  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Requests with modified user identifiers  
- Inconsistent user activity patterns  
- Unusual API behavior involving multiple user accounts  
- Logs showing actions performed across different user IDs  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Enforce strict **server-side authorization checks**  
- Ensure users can only act on their own resources  
- Avoid trusting **client-side input** for user identification  
- Implement proper **access control mechanisms** across all endpoints  

---

# Key Learning

This analysis highlights how improper authorization checks can allow attackers to manipulate data across user accounts.

Ensuring strong access control is essential to maintain data integrity and trust within applications.

---

# Screenshots

## Feedback Submission Request Interception
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_custo_feed.png)

## Modified Request with Different User ID
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_custo_feed1.png)

## Feedback Stored Under Another User
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_custo_feed2.png)
