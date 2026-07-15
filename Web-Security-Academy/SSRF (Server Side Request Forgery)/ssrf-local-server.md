# PortSwigger Lab Writeup

## Lab: Basic SSRF Against the Local Server – Apprentice

---

## Lab Overview

This lab demonstrates a **Server-Side Request Forgery (SSRF)** vulnerability in the stock check functionality.

The application fetches stock information by making server-side requests to a URL supplied by the `stockApi` parameter. Because the application does not validate the destination URL, an attacker can force the server to access internal resources that are not directly accessible.

The objective is to access the internal administration interface and delete the user `carlos`.

---

## Objective

- Identify an SSRF vulnerability
- Access the internal admin interface
- Delete the user `carlos`

---

## Tools Used

- Burp Suite
- Web Browser

---

## Exploitation Steps

1. Attempt to access the admin page directly:

```
http://localhost/admin
```

Access is denied because the page is only accessible internally.

2. Navigate to any product page.

3. Click **Check Stock**.

4. Intercept the request using Burp Suite and send it to Repeater.

5. Locate the `stockApi` parameter.

Example:

```
stockApi=http://stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1
```

6. Modify the parameter to:

```
http://localhost/admin
```

7. Send the request.

8. The response displays the internal administration interface.

9. Identify the endpoint used to delete the target user:

```
http://localhost/admin/delete?username=carlos
```

10. Replace the `stockApi` value with:

```
http://localhost/admin/delete?username=carlos
```

11. Send the request.

12. The user `carlos` is deleted, solving the lab.

---

## Screenshots

### 1. Original Stock Check Request
![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_1-2.png)

### 2. Accessing the Internal Admin Panel
![Admin Panel](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_1-3.png)

### 3. Delete User Request
![Delete User](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_1-4.png)

### 4. Lab Solved
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_1-5.png)

---

## Result

The vulnerable server made an HTTP request to its own localhost interface.

By exploiting the SSRF vulnerability, the internal administration panel became accessible, allowing the attacker to delete the user `carlos`.

---

## Vulnerability Explanation

This vulnerability occurs because the application allows user-controlled URLs to be requested by the server.

### 1. User-Controlled URL

The `stockApi` parameter determines where the server sends its HTTP request.

### 2. No URL Validation

The application does not verify whether the destination is trusted.

### 3. Internal Network Access

Since the request originates from the server itself, it can access internal services such as:

```
http://localhost
```

These services are normally inaccessible to external users.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `stockApi` | User-controlled request destination |
| Server-side request | Executed by the application |
| `http://localhost/admin` | Accesses internal admin panel |
| Internal trust | Server can access restricted resources |
| Delete endpoint | Removes the target user |

---

## Mitigation Techniques

### 1. Validate Destination URLs

Only allow requests to trusted domains and endpoints.

Use an allowlist instead of accepting arbitrary URLs.

---

### 2. Restrict Internal Network Access

Prevent application servers from making requests to:

- `localhost`
- `127.0.0.1`
- Internal IP ranges
- Cloud metadata services

---

### 3. Network Segmentation

Separate internal administration services from application servers.

---

### 4. Disable Unnecessary Server-Side Requests

Avoid allowing users to control backend request destinations whenever possible.

---

### 5. Monitor Outbound Requests

Log and monitor unusual outbound requests that target internal resources.

---

## Key Takeaways

- SSRF allows attackers to make requests from the vulnerable server.
- Internal services such as `localhost` can become accessible through SSRF.
- Sensitive administrative interfaces should never rely solely on network location for protection.
- Strict URL validation and network restrictions are essential to prevent SSRF attacks.

---

## Lab Status

Solved Successfully
