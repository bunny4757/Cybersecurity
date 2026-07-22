# PortSwigger Lab Writeup

## Lab: OS Command Injection, Simple Case – Apprentice

---

## Lab Overview

This lab demonstrates an **Operating System (OS) Command Injection** vulnerability in the product stock checker functionality.

The application executes a shell command using user-supplied input without proper validation or sanitization. As a result, an attacker can inject additional operating system commands that are executed by the server.

The objective is to execute the `whoami` command and identify the user account under which the application is running.

---

## Objective

- Identify an OS Command Injection vulnerability
- Inject an operating system command
- Execute the `whoami` command

---

## Tools Used

- Burp Suite
- Web Browser

---

## Exploitation Steps

1. Navigate to any product page.

2. Click **Check Stock**.

3. Intercept the request using Burp Suite.

4. Locate the `storeId` parameter.

Example:

```
storeId=1
```

5. Modify the parameter to:

```
1|whoami
```

6. Forward the request.

7. Observe the server response.

The response contains the username of the operating system account running the application.

---

## Screenshots

### 1. Original Stock Check Request
![Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/os_inject_lab1-1.png)

### 2. Injected Payload
![Payload](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/os_inject_lab1-2.png)

### 3. Command Execution Result
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/os_inject_lab1-3.png)

---

## Result

The injected command is executed by the operating system.

The application returns the output of the `whoami` command, revealing the user account under which the web application is running.

Example:

```
peter
```

*(The returned username may vary depending on the lab instance.)*

---

## Vulnerability Explanation

This vulnerability occurs because the application executes system commands using unsanitized user input.

### 1. User-Controlled Input

The `storeId` parameter is incorporated directly into a shell command.

### 2. Shell Command Execution

The application invokes an operating system shell to execute the command.

### 3. Command Injection

By using the pipe operator (`|`), an attacker appends an additional command to be executed.

As a result, arbitrary operating system commands can run with the privileges of the web application.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `storeId` | User-controlled input |
| `|` | Command separator in the shell |
| `whoami` | Displays the current operating system user |
| Shell execution | Executes the injected command |

---

## Mitigation Techniques

### 1. Avoid Executing System Commands

Whenever possible, use built-in programming language functions instead of shell commands.

---

### 2. Validate User Input

- Accept only expected values.
- Use allowlists for input validation.
- Reject special shell characters.

---

### 3. Use Parameterized APIs

If system commands must be executed, use APIs that separate commands from user input instead of invoking a shell.

---

### 4. Principle of Least Privilege

Run the application with a low-privileged operating system account to reduce the impact of successful command injection.

---

### 5. Secure Coding Practices

- Avoid string concatenation when building shell commands.
- Escape or sanitize user input when command execution is unavoidable.

---

## Key Takeaways

- OS Command Injection allows attackers to execute arbitrary operating system commands.
- Unsanitized user input should never be passed directly to a shell.
- Running applications with minimal privileges reduces the impact of exploitation.
- Input validation and avoiding shell execution are the most effective defenses.

---

## Lab Status

Solved Successfully
