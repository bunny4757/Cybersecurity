# PortSwigger Lab Writeup

## Lab: SQL Injection in WHERE Clause (Retrieving Hidden Data) – Apprentice

---

## Lab Overview
This lab demonstrates a classic SQL Injection vulnerability in a product category filter.

The application executes the following SQL query when a category is selected:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1;
```

The objective is to exploit this vulnerability to display unreleased (hidden) products.

---

## Objective
- Perform SQL Injection  
- Bypass the `released = 1` condition  
- Retrieve hidden/unreleased data  

---

## Tools Used
- Burp Suite  

---

## Exploitation Steps

1. Intercept the request using Burp Suite  
2. Locate the `category` parameter  
3. Modify the parameter value to:

```
'+OR+1=1--
```

4. Forward the request to the server  

---

## Result

The modified query becomes:

```sql
SELECT * FROM products WHERE category = '' OR 1=1--' AND released = 1;
```

- `OR 1=1` makes the condition always true  
- `--` comments out the remaining part of the query  

This causes the application to return all products, including unreleased ones.

---

## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_where_cause1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_where_cause2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/Sql_injection_Apprentice_where_cause3.png)

## Vulnerability Explanation

This vulnerability occurs due to improper handling of user input:

### 1. Unsanitized User Input
The application directly inserts user input into the SQL query without validation or escaping.

### 2. Dynamic Query Construction
The query is built using string concatenation, allowing attackers to inject SQL code.

### 3. Lack of Input Validation
Special characters such as `'` and `--` are not filtered or handled securely.

As a result, attackers can manipulate the logic of the query.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `'` | Closes the original string |
| `OR 1=1` | Always true condition |
| `--` | Comments out remaining query |

This bypasses the intended filter (`released = 1`).

---

## Mitigation Techniques

### 1. Use Parameterized Queries (Prepared Statements)
```sql
SELECT * FROM products WHERE category = ? AND released = 1;
```

### 2. Input Validation and Sanitization
- Validate user inputs strictly  
- Use allowlists instead of blocklists  

### 3. Use ORM Frameworks
Avoid manual SQL query construction by using secure ORM tools.

### 4. Principle of Least Privilege
Ensure database users have minimal required permissions.

### 5. Web Application Firewall (WAF)
Deploy a WAF to detect and block SQL injection attempts.

---

## Key Takeaways
- SQL Injection can expose sensitive or hidden data  
- Poor input handling leads to severe vulnerabilities  
- Always follow secure coding practices  

---

## Lab Status
Solved Successfully
