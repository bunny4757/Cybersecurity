# Web Security Analysis – Day 7
## Sensitive Information Disclosure via Image Metadata in OWASP Juice Shop

## Overview

This write-up documents **Day 7 of my Web Security Analysis series**, where I analyzed a **Sensitive Information Disclosure vulnerability via image metadata** that led to an **account takeover scenario** in the **OWASP Juice Shop** application.

Uploaded files such as images may contain hidden metadata, including GPS coordinates, timestamps, and device information. If exposed, attackers can use this data for reconnaissance or to bypass account recovery mechanisms.

---

# Target Application

- **Application:** OWASP Juice Shop  
- **Vulnerability Type:** Sensitive Information Disclosure  
- **Testing Environment:** Local Lab Environment  
- **Tools Used:** Burp Suite, Web Browser, ExifTool  

---

# Tools Used

- **Burp Suite** (Proxy & Repeater)  
- **Web Browser Developer Tools**  
- **ExifTool** for metadata analysis  
- **Manual Web Application Testing**

---

# Vulnerability Analysis

## Step 1 – Exploring the Photo Wall

While exploring the **Photo Wall section**, I identified an image uploaded by a user named Johnny.

I downloaded the image to analyze its contents for any hidden information.

---

## Step 2 – Extracting Image Metadata

Using **ExifTool**, I examined the metadata embedded within the image.

During analysis, I discovered **GPS coordinates** stored in the metadata.

---

## Step 3 – Using Extracted Information

The extracted GPS coordinates were used to identify a real-world location associated with the image.

This information appeared to be personal and potentially useful in other parts of the application.

---

## Step 4 – Exploiting Password Recovery

While testing the **password recovery functionality**, I attempted to reset Johnny’s account password.

One of the security questions asked about the user's **favorite hiking location**.

Using the location obtained from the image metadata, I was able to correctly answer the question and successfully reset the password.

---

## Step 5 – Identifying the Vulnerability

This demonstrates that sensitive information exposed through image metadata can be leveraged to bypass account recovery mechanisms.

The combination of **information disclosure and weak security questions** resulted in an **account takeover scenario**.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Extract sensitive information from uploaded files  
- Perform reconnaissance using exposed metadata  
- Bypass account recovery mechanisms  
- Gain unauthorized access to user accounts  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Unusual password reset attempts  
- Multiple account recovery requests  
- Suspicious login activity after password changes  
- Abnormal access patterns related to user accounts  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Remove or sanitize metadata from uploaded images  
- Avoid using easily discoverable information in security questions  
- Implement stronger account recovery mechanisms  
- Educate users about risks of sharing images with embedded location data  

---

# Key Learning

This analysis highlights how seemingly harmless data such as image metadata can expose sensitive information.

When combined with weak account recovery mechanisms, it can lead to serious security issues such as account takeover.

---

# Screenshots
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_photowall.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_photowall_exitmetadata.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_photowall_locationfinder.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_photowall_sucess.png)
