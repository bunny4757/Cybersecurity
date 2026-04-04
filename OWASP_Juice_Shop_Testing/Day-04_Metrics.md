# Web Security Analysis – Day 4
## Information Disclosure via Exposed Metrics Endpoint in OWASP Juice Shop

## Overview

This write-up documents **Day 4 of my Web Security Analysis series**, where I analyzed an **Information Disclosure vulnerability via an exposed metrics endpoint** while testing the **OWASP Juice Shop** application.

Modern web applications often include internal monitoring endpoints to track performance and system metrics. If these endpoints are publicly accessible without proper restrictions, they may expose sensitive internal information about the application.

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

## Step 1 – Exploring Application Endpoints

While testing the application, I explored different endpoints to understand the available API structure.

During this process, I interacted with the `/rest` endpoint and experimented with URL manipulation to identify additional accessible paths.

---

## Step 2 – Discovering the Metrics Endpoint

While modifying and testing different endpoints, I discovered the following path:

```
/metrics
```

Accessing this endpoint revealed detailed application metrics and internal monitoring data.

---

## Step 3 – Analyzing the Response

The `/metrics` endpoint exposed internal system information that is typically intended for monitoring tools or administrators.

This included insights into application performance and operational metrics, which should not be publicly accessible.

---

## Step 4 – Identifying the Vulnerability

The availability of the `/metrics` endpoint without authentication confirms an **Information Disclosure vulnerability**.

This endpoint exposes sensitive internal data due to improper access control and lack of restriction on monitoring endpoints.

---

# Potential Impact

If exploited in real-world applications, attackers could potentially:

- Gather internal system information  
- Understand application behavior and performance patterns  
- Identify technologies and services used by the application  
- Use exposed data for further reconnaissance and targeted attacks  

---

# Detection Perspective

Security teams may detect such activity by monitoring:

- Unauthorized access attempts to monitoring endpoints  
- Requests to uncommon paths such as `/metrics`, `/debug`, or `/admin`  
- Abnormal traffic targeting internal API routes  
- Suspicious enumeration of application endpoints  

---

# Mitigation Strategies

To prevent such vulnerabilities, developers should implement:

- Restrict access to monitoring endpoints using authentication  
- Limit exposure of internal metrics to trusted networks only  
- Disable unused monitoring endpoints in production environments  
- Implement proper access control and endpoint protection  

---

# Key Learning

This analysis highlights how publicly exposed internal endpoints can unintentionally reveal sensitive system information.

Proper access control and endpoint restriction are essential to prevent attackers from leveraging such information for reconnaissance and further exploitation.

---

# Screenshots

### Accessing /metrics Endpoint
![](https://github.com/bunny4757/Cybersecurity/blob/main/OWASP_Juice_Shop_Testing/Images/OJS_Metrics.png)
