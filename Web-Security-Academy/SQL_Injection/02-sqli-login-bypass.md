# PortSwigger Lab Writeup

## Lab: SQL Injection Vulnerability Allowing Login Bypass – Apprentice

---

## Lab Overview
This lab demonstrates a SQL Injection vulnerability in the login functionality.

The application performs a SQL query to verify user credentials during login. Due to improper input handling, this functionality is vulnerable to injection attacks.

The objective is to bypass authentication and log in as the administrator user.

---

## Objective
- Exploit SQL Injection in login form  
- Bypass authentication  
- Log in as `administrator`  

---

## Tools Used
- Burp Suite  

---

## Exploitation Steps

1. Intercept the login request using Burp Suite  
2. Locate the `username` and `password` parameters  
3. Modify the `username` parameter to:

```
administrator'--
```

4. Forward the request to the server  

---

## Screenshots

### 1. Intercepted Login Request
![Intercepted Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_login_bypass1.png)

### 2. Injected Payload
![Payload](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_login_bypass2.png)

### 3. Successful Login as Administrator
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_login_bypass3.png)

---

## Result

The injected query becomes:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = 'anything';
```

- `'` closes the username string  
- `--` comments out the password check  

This allows login without knowing the password.

---

## Vulnerability Explanation

This vulnerability occurs due to improper handling of user input in authentication logic.

### 1. Unsanitized Input
User input is directly inserted into the SQL query without validation.

### 2. Improper Authentication Logic
The application relies on database query results for authentication without securing the query.

### 3. Comment Injection
The attacker uses SQL comment (`--`) to remove the password condition.

As a result, authentication is bypassed.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `'` | Closes the string |
| `administrator` | Targets admin account |
| `--` | Comments out password check |

This makes the query validate only the username.

---

## Mitigation Techniques

### 1. Use Parameterized Queries (Prepared Statements)
```sql
SELECT * FROM users WHERE username = ? AND password = ?;
```

### 2. Input Validation
- Reject unexpected characters  
- Enforce strict input formats  

### 3. Password Hashing
- Store hashed passwords (e.g., bcrypt)  
- Never store plain text passwords  

### 4. Use Secure Authentication Logic
- Do not rely solely on SQL query results  
- Implement proper session management  

### 5. Web Application Firewall (WAF)
Detect and block SQL injection attempts  

---

## Key Takeaways
- SQL Injection can completely bypass authentication  
- Login forms are high-risk targets  
- Secure query handling is critical  

---

## Lab Status
Solved Successfully
