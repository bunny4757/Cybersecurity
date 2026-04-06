# Web Security Analysis – Day 15
## Information Disclosure via Exposed Backup File in OWASP Juice Shop

## Overview

This write-up documents **Day 15 of my Web Security Analysis series**, where I analyzed an **Information Disclosure vulnerability** caused by an exposed developer backup file in the **OWASP Juice Shop** application.

Backup files left on production servers can expose sensitive information if proper validation and access controls are not implemented.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Information Disclosure  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Exploring FTP Directory

While exploring the **/ftp/** directory, I identified the presence of a backup file.

Although direct access to the file was restricted, it indicated the possibility of sensitive data exposure.

---

## Step 2 – Testing Input Validation

To understand how the application validates file access, I intercepted the request using **Burp Suite Proxy** and sent it to **Burp Suite Repeater**.

I then analyzed how the application validates file extensions and access permissions.

---

## Step 3 – Bypassing Access Controls

While testing file access restrictions, I modified the request by appending a **double-encoded null byte**:

```
%2500
```

This resulted in a payload such as:

```
file.md%2500.png
```

After server-side decoding, the input was interpreted as:

```
file.md%00.png
```

This allowed me to bypass file validation checks, as the application validated the `.png` extension but processed the file as `.md`.

Using this technique, I successfully accessed and downloaded the restricted backup file.

---

## Step 4 – Identifying the Vulnerability

The downloaded file contained sensitive data, confirming that the application does not properly validate file access or restrict access to backup resources.

This demonstrates an **Information Disclosure vulnerability due to weak input validation and improper file access control**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Access sensitive backup or configuration files  
- Retrieve internal application data  
- Expose credentials or system information  
- Use the data for further exploitation  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Requests attempting to access backup or hidden files  
- Suspicious encoded or manipulated input in requests  
- Unusual file download patterns  
- Access attempts to restricted directories  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Remove backup files from production environments  
- Enforce strict **input validation** and file access controls  
- Validate file extensions after full decoding of input  
- Restrict access to sensitive files using proper **authorization checks**  
- Store backups securely outside publicly accessible directories  

---

# Key Learning

This analysis highlights how weak validation combined with encoding-based bypass techniques can lead to serious information disclosure risks.

Understanding how encoding and input validation interact is critical in identifying and preventing such vulnerabilities.

---

# Series Completion

With this write-up, I have completed a **15-day Web Security Analysis series**, covering key vulnerabilities such as:

- Cross-Site Scripting (XSS)  
- SQL Injection  
- Broken Access Control  
- Insecure Direct Object Reference (IDOR)  
- Information Disclosure  
- Privilege Escalation  

These analyses were performed using **Burp Suite**, **Postman**, and manual testing techniques, demonstrating practical web application security testing skills.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_frogotten_backup1.png)

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_frogotten_backup2.png)

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_frogotten_backup3.png)

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_frogotten_backup4.png)
