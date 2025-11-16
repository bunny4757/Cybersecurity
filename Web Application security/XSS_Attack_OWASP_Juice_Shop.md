#  Cross-Site Scripting (XSS) Attack on OWASP Juice Shop

##  Objective
The goal of this assignment is to perform a safe and controlled **Cross-Site Scripting (XSS)** attack on the purposely vulnerable web application **OWASP Juice Shop**, using a harmless JavaScript payload to demonstrate how unsanitized user input can lead to code execution inside the browser.

---

##  Tools Used
- **OWASP Juice Shop**
- **Web Browser**
- **Burp Suite Community Edition** (optional, for observing the request)

---

##  Step-by-Step Procedure

###  Step 1 — Open OWASP Juice Shop
The Juice Shop environment was accessed in a controlled, legal setting.  
A user input field (such as the review, feedback, or search field) was selected for testing.


---

###  Step 2 — Enter XSS Payload
To test if the input was vulnerable, the following harmless XSS payload was entered:
<iframe src=javascript:alert('XSS')></iframe>
This payload attempts to execute a JavaScript alert() function by embedding it inside an iframe.

If the application does not sanitize input, the script will execute in the user’s browser.

###  Step 3 — Triggering the XSS Attack
After submitting the payload, the application reflected it back into the webpage without filtering or escaping it.
As a result, the JavaScript code executed and displayed a popup box.
This confirms a stored or reflected XSS vulnerability, depending on where the input was submitted.



###  Understanding the XSS Vulnerability
Cross-Site Scripting (XSS) occurs when user-controlled input is inserted into a webpage without proper sanitization or HTML escaping, allowing attackers to inject JavaScript that executes inside the victim’s browser. This vulnerability can lead to serious security issues such as arbitrary JavaScript execution, cookie theft, session hijacking, user redirection, UI manipulation, and unauthorized actions. In this assignment, the alert popup clearly demonstrated that the application executed the injected JavaScript code, confirming the presence of an XSS vulnerability.

###  Screenshots to Include
![xxs input](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/xssscript.png)
![xxs output](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/alertban.png)
![challenge completion](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/alertjsjuiceshop.png)

###  What This Demonstrates
Lack of input sanitization

Failure to escape HTML tags

Vulnerability to client-side code execution

Real-world risks such as session hijacking, cookie theft, and UI manipulation

OWASP Juice Shop intentionally includes this flaw for training purposes.

###  Conclusion
In this assignment, a Cross-Site Scripting (XSS) attack was successfully performed on OWASP Juice Shop using the payload:

<iframe src=javascript:alert('XSS')></iframe>
The browser executed the injected JavaScript and displayed an alert box, confirming the presence of an XSS vulnerability. This highlights the importance of proper input sanitization and output encoding in web applications.
