# PortSwigger Lab Writeup

## Lab: DOM XSS in document.write Sink Using location.search – Apprentice

---

## Lab Overview
This lab demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in the search functionality.

The application uses JavaScript `document.write()` to write user-controlled data from `location.search` directly into the HTML without sanitization.

The objective is to inject JavaScript that executes in the browser.

---

## Objective
- Identify DOM-based XSS vulnerability  
- Exploit client-side JavaScript execution  
- Execute the `alert()` function  

---

## Tools Used
- Web Browser  
- Developer Tools (Inspect Element)  

---

## Exploitation Steps

1. Enter a random string in the search box  
2. Right-click and inspect the page  
3. Observe the input reflected inside an `<img>` tag (e.g., `src` attribute)  
4. Modify the payload in the URL to:

```
"><svg onload=alert(1)>
```

5. Reload or access the crafted URL  

---

## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_documetwrite1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_documetwrite2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_documetwrite3.png)

---

## Result

- The payload breaks out of the HTML attribute  
- A malicious `<svg>` tag is injected  
- The `onload` event executes JavaScript  
- An alert box appears, confirming successful DOM XSS  

---

## Vulnerability Explanation

This vulnerability occurs due to unsafe handling of user-controlled data in client-side JavaScript.

### 1. Unsafe Sink (document.write)
The application uses `document.write()` to insert data directly into the DOM.

### 2. Controllable Source (location.search)
User input from the URL query string is directly used without validation.

### 3. No Sanitization
The input is not encoded or filtered before being written to the page.

As a result, attackers can inject arbitrary HTML/JavaScript.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `location.search` | User-controlled input source |
| `document.write()` | Writes directly to DOM |
| `">` | Breaks out of attribute |
| `<svg onload=alert(1)>` | Executes JavaScript |

This allows execution of arbitrary scripts in the browser.

---

## Mitigation Techniques

### 1. Avoid document.write()
- Use safer DOM methods like `textContent` or `innerText`  

### 2. Input Validation and Encoding
- Properly sanitize and encode user input before rendering  

### 3. Use Safe DOM APIs
- Prefer `createElement()` and `setAttribute()`  

### 4. Content Security Policy (CSP)
- Restrict execution of inline JavaScript  

### 5. Secure Coding Practices
- Avoid directly using user input in the DOM  

---

## Key Takeaways
- DOM XSS occurs entirely on the client side  
- Unsafe sinks like `document.write()` are dangerous  
- Always validate and encode user-controlled data  

---

## Lab Status
Solved Successfully
