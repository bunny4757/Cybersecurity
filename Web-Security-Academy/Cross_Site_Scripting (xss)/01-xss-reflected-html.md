# PortSwigger Lab Writeup

## Lab: Reflected XSS into HTML Context with No Encoding – Apprentice

---

## Lab Overview
This lab demonstrates a reflected Cross-Site Scripting (XSS) vulnerability in the search functionality.

The application reflects user input directly into the HTML response without any encoding or sanitization.

The objective is to inject JavaScript that executes in the browser.

---

## Objective
- Identify reflected XSS vulnerability  
- Inject malicious JavaScript  
- Execute the `alert()` function  

---

## Tools Used
- Web Browser  

---

## Exploitation Steps

1. Navigate to the search functionality  
2. Enter the following payload in the search box:

```
<script>alert(1)</script>
```

3. Click on "Search"  

---

## Screenshots

### 1. Injected Payload in Search Box
![Payload](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Xss_reflected_html_no_encoding.png)

### 2. Alert Popup Execution
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Xss_reflected_html_no_encoding2.png)

### 3. Labsolved
![solved](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Xss_reflected_html_no_encoding3.png)

---

## Result

- The payload is reflected directly into the HTML response  
- The browser executes the injected JavaScript  
- An alert box appears confirming successful XSS  

---

## Vulnerability Explanation

This vulnerability occurs due to improper handling of user input in the HTML context.

### 1. No Output Encoding
User input is directly embedded into the HTML response without encoding special characters.

### 2. Reflected Input
The input is immediately returned in the server response, making it a reflected XSS.

### 3. Execution in Browser
Browsers interpret the injected `<script>` tag as executable JavaScript.

As a result, attackers can execute arbitrary scripts in the victim's browser.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `<script>` | Defines executable JavaScript block |
| `alert(1)` | Test payload for execution |
| No encoding | Allows script to run |

---

## Mitigation Techniques

### 1. Output Encoding
- Encode special characters (`<`, `>`, `"`, `'`) before rendering  

### 2. Input Validation
- Restrict and validate user input  

### 3. Content Security Policy (CSP)
- Prevent execution of inline scripts  

### 4. Use Secure Frameworks
- Modern frameworks automatically escape output  

---

## Key Takeaways
- Reflected XSS occurs when user input is returned without encoding  
- Even simple inputs can lead to script execution  
- Always sanitize and encode output  

---

## Lab Status
Solved Successfully
