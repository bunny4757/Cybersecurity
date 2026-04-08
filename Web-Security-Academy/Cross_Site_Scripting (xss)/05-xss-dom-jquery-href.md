# PortSwigger Lab Writeup

## Lab: DOM XSS in jQuery Anchor href Attribute Sink Using location.search – Apprentice

---

## Lab Overview
This lab demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in the feedback functionality.

The application uses the jQuery `$()` selector to modify the `href` attribute of an anchor (`<a>`) element using data from `location.search`.

The objective is to inject a payload that executes JavaScript when the "Back" link is clicked.

---

## Objective
- Identify DOM-based XSS vulnerability  
- Exploit unsafe jQuery attribute manipulation  
- Execute JavaScript to display `document.cookie`  

---

## Tools Used
- Web Browser  
- Developer Tools (Inspect Element)  

---

## Exploitation Steps

1. Navigate to the "Submit feedback" page  
2. Modify the URL parameter `returnPath` with a random value:
```
/random123
```

3. Inspect the page and observe the value reflected inside the `<a href>` attribute  

4. Modify the `returnPath` parameter to:
```
javascript:alert(document.cookie)
```

5. Press Enter to load the URL  
6. Click on the "Back" link  

---

## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_jquery_href1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_jquery_href2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_jquery_href3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/DOM_xss_jquery_href4.png)


---

## Result

- The payload is injected into the `href` attribute  
- The link becomes a JavaScript execution context  
- Clicking "Back" executes the payload  
- An alert box displays `document.cookie`, confirming successful DOM XSS  

---

## Vulnerability Explanation

This vulnerability occurs due to unsafe handling of user-controlled input in client-side JavaScript.

### 1. Controllable Source (location.search)
User input from the URL is directly used without validation.

### 2. Unsafe Sink (href Attribute)
The application assigns user input directly to the `href` attribute.

### 3. jQuery Manipulation
The `$()` function is used to dynamically modify DOM elements without sanitization.

As a result, attackers can inject `javascript:` URLs and execute arbitrary code.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `location.search` | User-controlled input |
| `href` attribute | Execution context for links |
| `javascript:` | Executes JavaScript code |
| `alert(document.cookie)` | Displays sensitive data |

This allows execution of arbitrary JavaScript when the link is clicked.

---

## Mitigation Techniques

### 1. Validate URL Schemes
- Allow only safe protocols (`http`, `https`)  
- Block `javascript:` scheme  

### 2. Input Sanitization
- Sanitize and validate all user inputs  

### 3. Use Safe DOM APIs
- Avoid directly assigning user input to attributes  

### 4. Content Security Policy (CSP)
- Restrict execution of inline JavaScript  

### 5. Secure jQuery Usage
- Avoid unsafe DOM manipulation with untrusted data  

---

## Key Takeaways
- DOM XSS can occur through attribute manipulation  
- `javascript:` URLs are a common attack vector  
- Always validate and sanitize user-controlled input  

---

## Lab Status
Solved Successfully
