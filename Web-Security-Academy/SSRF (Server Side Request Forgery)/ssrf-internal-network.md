# PortSwigger Lab Writeup

## Lab: Basic SSRF Against Another Back-End System – Apprentice

---

## Lab Overview

This lab demonstrates a **Server-Side Request Forgery (SSRF)** vulnerability in the stock check functionality.

The application makes server-side requests based on the user-controlled `stockApi` parameter. By modifying this parameter, an attacker can force the server to communicate with internal systems that are inaccessible from the internet.

The objective is to discover an internal administration interface running on the `192.168.0.X` network and delete the user `carlos`.

---

## Objective

- Identify an SSRF vulnerability
- Enumerate the internal network
- Locate the administration interface
- Delete the user `carlos`

---

## Tools Used

- Burp Suite
- Burp Intruder
- Burp Repeater
- Web Browser

---

## Exploitation Steps

1. Navigate to any product page.

2. Click **Check Stock**.

3. Intercept the request using Burp Suite.

4. Send the request to **Burp Intruder**.

5. Locate the `stockApi` parameter and modify it as follows:

```
http://192.168.0.1:8080/admin
```

6. Highlight the last octet (`1`) of the IP address and click **Add §** to create a payload position.

7. In the **Payloads** tab, configure the payload:

```
Payload Type: Numbers

From: 1
To: 255
Step: 1
```

8. Start the Intruder attack.

9. Sort the responses by **Status Code**.

10. Identify the request returning **HTTP 200 OK**.

11. Send that successful request to **Burp Repeater**.

12. Modify the `stockApi` parameter to:

```
http://192.168.0.X:8080/admin/delete?username=carlos
```

> Replace `X` with the IP address that returned the `200 OK` response.

13. Send the request.

14. The user `carlos` is deleted, solving the lab.

---

## Screenshots

### 1. Original Stock Check Request
![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-1.png)

### 2. Burp Intruder Configuration
![Intruder](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-2.png)

### 3. Internal Host Discovery
![Host Discovery](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-3.png)
![Host Discovery](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-4.png)
### 4. Delete User Request
![Delete User](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-5.png)

### 5. Lab Solved
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/ssrf_lab_2-6.png)

---

## Result

The vulnerable application was used to scan the internal network.

An internal administration interface was discovered on one of the `192.168.0.X` hosts. Using the SSRF vulnerability, the delete endpoint was accessed and the user `carlos` was successfully removed.

---

## Vulnerability Explanation

This vulnerability occurs because the application allows user-controlled URLs to be requested by the server.

### 1. User-Controlled Backend Requests

The application trusts the value supplied in the `stockApi` parameter.

### 2. Internal Network Access

Since requests originate from the server, they can access internal IP addresses that are unreachable from external users.

### 3. Internal Network Enumeration

By changing the destination IP address, attackers can discover internal hosts and services.

### 4. Access to Administrative Services

Once an internal administrative interface is found, privileged actions can be performed through SSRF.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `stockApi` | User-controlled request destination |
| Burp Intruder | Automates IP address scanning |
| `192.168.0.X` | Internal network range |
| HTTP 200 Response | Indicates the admin interface |
| Delete endpoint | Removes the target user |

---

## Mitigation Techniques

### 1. Validate Destination URLs

Allow requests only to trusted domains or specific backend services.

Implement an allowlist instead of accepting arbitrary URLs.

---

### 2. Restrict Access to Internal Networks

Block requests to:

- `127.0.0.1`
- `localhost`
- `192.168.0.0/16`
- `10.0.0.0/8`
- `172.16.0.0/12`
- Cloud metadata services

---

### 3. Network Segmentation

Ensure internal administrative interfaces are isolated from application servers.

---

### 4. Restrict Outbound Requests

Use firewall rules to prevent applications from accessing unauthorized internal systems.

---

### 5. Monitor SSRF Indicators

Detect unusual outbound requests, internal IP scanning, and repeated requests to internal resources.

---

## Key Takeaways

- SSRF can be used to enumerate internal networks.
- Internal administrative interfaces should never rely solely on private IP addresses for protection.
- Attackers can combine SSRF with automated scanning tools to discover hidden services.
- URL validation, network restrictions, and proper segmentation are essential defenses against SSRF.

---

## Lab Status

Solved Successfully
