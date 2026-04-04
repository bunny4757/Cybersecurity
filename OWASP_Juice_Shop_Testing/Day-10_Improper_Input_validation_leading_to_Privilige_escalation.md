# Web Security Analysis – Day 10
## Improper Input Validation Leading to Privilege Escalation in OWASP Juice Shop

## Overview

This write-up documents **Day 10 of my Web Security Analysis series**, where I analyzed an **Improper Input Validation vulnerability leading to Privilege Escalation** in the **OWASP Juice Shop** application.

Improper Input Validation occurs when an application fails to validate or restrict user-supplied data on the server side. This can allow attackers to manipulate request parameters and gain unauthorized privileges.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Improper Input Validation / Privilege Escalation  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Intercepting Registration Request

While registering a new user account, I intercepted the request using **Burp Suite Proxy** and forwarded it to **Burp Suite Repeater** for further analysis.

This allowed me to examine how user details were being sent to the server.

---

## Step 2 – Analyzing Request Parameters

During analysis, I observed the structure of the request and how user attributes were handled by the backend.

To test input validation, I attempted to modify the request by introducing an additional parameter related to user roles.

---

## Step 3 – Manipulating Input Data

I added a role-related parameter to the registration request and resent it to the server using **Burp Suite Repeater**.

The application accepted the modified request without validating or restricting the input.

---

## Step 4 – Identifying the Vulnerability

After successful registration, the newly created account was assigned elevated privileges.

This confirms that the application trusts user-controlled input and does not enforce proper validation or role-based restrictions.

This behavior demonstrates an **Improper Input Validation vulnerability leading to Privilege Escalation**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Escalate privileges from a normal user to an administrator  
- Gain unauthorized access to restricted functionalities  
- Manipulate or control sensitive application features  
- Compromise overall application security  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Unusual parameters in registration or API requests  
- Unexpected role assignments in user accounts  
- Abnormal privilege changes in logs  
- Suspicious request manipulation patterns  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Enforce strict **server-side validation** of all inputs  
- Do not allow client-side control over sensitive fields such as roles  
- Implement proper **role-based access control (RBAC)**  
- Validate and sanitize all incoming request parameters  

---

# Key Learning

This analysis highlights how improper input validation can lead to privilege escalation.

Allowing user-controlled data to influence sensitive attributes such as roles can result in unauthorized administrative access and compromise application security.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_adminregis1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_adminregis4.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_adminregis2.png)
