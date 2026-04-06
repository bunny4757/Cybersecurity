# Web Security Analysis – Day 14
## Information Disclosure via Exposed Directories and Log Files in OWASP Juice Shop

## Overview

This write-up documents **Day 14 of my Web Security Analysis series**, where I analyzed an **Information Disclosure vulnerability** caused by exposed directories and log files in the **OWASP Juice Shop** application.

Information Disclosure vulnerabilities occur when sensitive files or directories are accessible without proper access restrictions, exposing internal data such as logs, configurations, or system information.

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

## Step 1 – Exploring Known Directories

While testing the application, I revisited the previously identified **/ftp/** directory discovered through URL manipulation.

This directory served as a starting point for further exploration of accessible internal resources.

---

## Step 2 – Directory Enumeration

During further exploration, I identified references to additional internal files.

Using directory enumeration techniques, I discovered a **logs directory** within the application.

---

## Step 3 – Accessing Log Files

By modifying the URL and navigating to the identified path, I accessed a logs-related endpoint and downloaded an **access log file**.

---

## Step 4 – Identifying the Vulnerability

Upon analyzing the downloaded file, it contained internal application request logs, including system activity data.

This confirms that sensitive operational data was exposed without proper access control, demonstrating an **Information Disclosure vulnerability**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Access sensitive log files containing system activity  
- Gather internal application details for reconnaissance  
- Identify endpoints, tokens, or user activity patterns  
- Use the information for further targeted attacks  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Requests to hidden or uncommon directories (e.g., logs, backups)  
- Repeated directory enumeration or fuzzing attempts  
- Unusual file download activity  
- Suspicious access to internal resources  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Restrict access to sensitive directories and files  
- Disable **directory listing** on servers  
- Store logs outside publicly accessible paths  
- Implement proper **authentication and authorization** for internal resources  

---

# Key Learning

This analysis highlights how exposed directories and log files can unintentionally leak sensitive information.

Attackers can leverage such data for deeper reconnaissance and further exploitation of the application.

---

# Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_accesslog1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_accesslog2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_accesslog3.png)
