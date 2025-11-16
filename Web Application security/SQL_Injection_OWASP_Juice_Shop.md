# SQL Injection on OWASP Juice Shop

##  Objective
The goal of this assignment is to demonstrate a safe and controlled SQL Injection attack on OWASP Juice Shop by injecting malicious input into the login form and gaining unauthorized access to the administrator account.

---

##  Tools Used
- **OWASP Juice Shop** (vulnerable web application)
- **Burp Suite Community Edition** (to observe request details)
- **Web Browser**

---

## Step-by-Step Procedure

###  Step 1 — Open OWASP Juice Shop
The Juice Shop application was opened in a controlled environment.  

---

###  Step 2 — Perform SQL Injection on the Login Form
A classic training-safe SQL Injection payload was entered in the **email field** to bypass authentication:

' OR 1=1--

 
 

This payload forces the login query to always return **true**, allowing login without a valid password.

The login request was captured in Burp Suite, where the returned authentication token showed the **admin email**, confirming unauthorized admin access.

---

### Step 3 — Logged in as Administrator
After submitting the SQL injection payload, the application logged into the **Administrator account**, proving that the login form is vulnerable to SQL Injection.


---

##  How This Attack Works (Simple Explanation)
SQL Injection happens when user input is not properly validated.  
The payload:

' OR 1=1--

 
 

breaks the SQL query and makes it:

- Always true  
- Skip password checking  
- Return the first user in the database (which is often **admin**)  

This allows an attacker to access accounts without valid credentials.

---

## Screenshots Included
![Sql injection login form](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/sqlinject.png)
![Burp authentication token](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/bruiplogin.png)
![logged in as admin](https://github.com/bunny4757/Cybersecurity/blob/main/Web%20Application%20security/Images/loginasadmin.png)


##  What This Demonstrates
This assignment successfully proves:

- The login form is vulnerable to SQL Injection  
- Input validation is missing  
- Authentication can be bypassed  
- Sensitive information (like JWT token & admin email) can be retrieved  

SQL Injection is one of the most severe OWASP Top 10 vulnerabilities.

---

##  Conclusion
In this assignment, SQL Injection was performed on OWASP Juice Shop using a simple payload in the login form. Burp Suite confirmed the authentication token and admin email, and the application granted administrator access.  
This demonstrates how dangerous SQL Injection can be when applications fail to validate user input.

