# PortSwigger Lab Writeup

## Lab: DOM XSS in innerHTML Sink Using location.search – Apprentice

---

## Lab Overview
This lab demonstrates a DOM-based Cross-Site Scripting (XSS) vulnerability in the search blog functionality.

The application uses `innerHTML` to insert user-controlled data from `location.search` directly into the DOM without sanitization.

The objective is to inject JavaScript that executes in the browser.

---

## Objective
- Identify DOM-based XSS vulnerability  
- Exploit unsafe `innerHTML` usage  
- Execute the `alert()` function  

---

## Tools Used
- Web Browser  
- Developer Tools (Inspect Element)  

---

## Exploitation Steps

1. Navigate to the search functionality  
2. Enter the following payload in the search box:

```
<img src=1 onerror=alert(1)>
```

3. Click "Search"  

---

## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Dom_xss_innterhtml_sink_locationsearch.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Dom_xss_innterhtml_sink_locationsearch1.png)

---

## Result

- The payload is inserted into the DOM using `innerHTML`  
- The invalid `src` attribute triggers an error  
- The `onerror` event executes JavaScript  
- An alert box appears, confirming successful DOM XSS  

---

## Vulnerability Explanation

This vulnerability occurs due to unsafe handling of user input in client-side JavaScript.

### 1. Unsafe Sink (innerHTML)
The application uses `innerHTML` to dynamically update the DOM with user input.

### 2. Controllable Source (location.search)
User input from the URL query string is directly used without validation.

### 3. No Sanitization
The input is not encoded or filtered before being inserted into the DOM.

As a result, attackers can inject malicious HTML/JavaScript.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `location.search` | User-controlled input source |
| `innerHTML` | Inserts raw HTML into DOM |
| `<img src=1>` | Invalid source triggers error |
| `onerror=alert(1)` | Executes JavaScript |

This allows execution of arbitrary scripts in the browser.

---

## Mitigation Techniques

### 1. Avoid innerHTML for Untrusted Data
- Use `textContent` or `innerText` instead  

### 2. Input Validation and Encoding
- Sanitize and encode all user inputs  

### 3. Use Safe DOM APIs
- Use `createElement()` and `setAttribute()`  

### 4. Content Security Policy (CSP)
- Restrict execution of inline scripts  

### 5. Secure Development Practices
- Never trust client-side input  

---

## Key Takeaways
- DOM XSS occurs entirely in the browser  
- `innerHTML` is a high-risk sink  
- Proper input handling is critical for security  

---

## Lab Status
Solved Successfully
