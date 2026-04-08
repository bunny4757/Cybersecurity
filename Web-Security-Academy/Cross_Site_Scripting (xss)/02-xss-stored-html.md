# PortSwigger Lab Writeup

## Lab: Stored XSS into HTML Context with No Encoding – Apprentice

---

## Lab Overview
This lab demonstrates a stored Cross-Site Scripting (XSS) vulnerability in the comment functionality.

The application stores user input and later renders it in the browser without encoding or sanitization.

The objective is to inject JavaScript that executes when the blog post is viewed.

---

## Objective
- Identify stored XSS vulnerability  
- Inject persistent malicious JavaScript  
- Execute the `alert()` function on page load  

---

## Tools Used
- Web Browser  

---

## Exploitation Steps

1. Navigate to the blog post comment section  
2. Enter the following payload in the comment box:

```
<script>alert(1)</script>
```

3. Fill in required fields (name, email, website)  
4. Click "Post comment"  
5. Revisit or refresh the blog post page  

---

## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Xss_stored_no_encoding.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Xss_stored_no_encoding2.png)

---

## Result

- The payload is stored in the application database  
- When the blog is viewed, the script is executed  
- An alert box appears, confirming successful stored XSS  

---

## Vulnerability Explanation

This vulnerability occurs due to improper handling of stored user input.

### 1. No Output Encoding
User input is stored and rendered without encoding special characters.

### 2. Persistent Execution
The malicious script is executed every time the page is loaded.

### 3. Stored Input in Database
The payload is saved server-side, making it more dangerous than reflected XSS.

As a result, multiple users can be affected.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `<script>` | Executes JavaScript in browser |
| `alert(1)` | Proof of execution |
| No encoding | Allows script execution |
| Stored input | Executes for every visitor |

---

## Mitigation Techniques

### 1. Output Encoding
- Encode special characters before rendering user input  

### 2. Input Sanitization
- Remove or neutralize dangerous HTML/JavaScript  

### 3. Content Security Policy (CSP)
- Restrict execution of inline scripts  

### 4. Use Secure Frameworks
- Automatically escape user-generated content  

### 5. Validate and Store Safely
- Sanitize input before storing in the database  

---

## Key Takeaways
- Stored XSS is more dangerous than reflected XSS  
- Malicious scripts persist and affect multiple users  
- Proper encoding and sanitization are critical  

---

## Lab Status
Solved Successfully
