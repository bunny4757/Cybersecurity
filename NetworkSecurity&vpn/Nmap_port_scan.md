# Nmap Port Scanning and Service Identification

## Objective
The goal of this assignment is to use **Nmap**, a popular network scanning tool, to scan a target machine for open ports, identify the services running on those ports, and explain what those services are used for.

---

## Step-by-Step Procedure

### Step 1 — Install Nmap
If Nmap is not installed, run:

sudo apt update
sudo apt install nmap -y

 
 

Nmap will now be ready for scanning.

---

### Step 2 — Choose a Target Machine
For this assignment, the target machine’s public IP address is:

163.70.140.35

 
 

**Note:** This scan was done only for educational purposes on a test environment.  
Unauthorized scanning of public IPs is not allowed and can be illegal.

---

###  Step 3 — Perform a Version Scan
To scan for open ports and detect running services, the following Nmap command was executed:

nmap -sV 163.70.140.35

 
 

**Flags used:**
- `-sV` → Detect service and version information

---

## Nmap Scan Results

The scan returned the following open ports and services:

PORT STATE SERVICE VERSION
80/tcp open tcpwrapped
|http-server-header: proxygen-bolt
443/tcp open tcpwrapped
| tls-alpn:
| h2
| http/1.1

 
 

This means two ports were detected as open:

- **Port 80 (HTTP)**  
- **Port 443 (HTTPS)**  

Both are reported as `tcpwrapped`, meaning the server is responding but not revealing full service details.

---

## Explanation of Services Running on Identified Ports

### **1️⃣ Port 80 — HTTP (Hypertext Transfer Protocol)**
- Used for unencrypted web traffic  
- Allows users to access websites using standard HTTP  
- Commonly used for serving web pages, APIs, and redirects  
- In this scan, the server header revealed:

http-server-header: proxygen-bolt

 
 

**Proxygen** is a high-performance HTTP framework developed by Facebook (Meta), often used in load balancers or proxies.

---

### **2️⃣ Port 443 — HTTPS (HTTP Secure)**
- Used for encrypted web traffic  
- Ensures secure communication using TLS/SSL  
- Most modern websites run HTTPS for login pages, banking, e-commerce, etc.

Nmap detected ALPN protocols:

h2
http/1.1

 
 

This means:

- `h2` → Supports HTTP/2  
- `http/1.1` → Supports older HTTP/1.1  

Both protocols are served over encrypted TLS.

---

## Screenshot
![nmap](https://github.com/bunny4757/Cybersecurity/blob/main/NetworkSecurity%26vpn/images/nmap.png)

 
 

---

## Understanding This Tool
Nmap is a powerful tool used by cybersecurity analysts to:

- Identify open ports  
- Enumerate services  
- Detect potential vulnerabilities  
- Understand attack surfaces  

Scanning ports 80 and 443 reveals how web servers expose services over the internet.

---

## Conclusion
In this assignment, Nmap was used to scan the target machine at **163.70.140.35**.  
Two open ports were found — **80 (HTTP)** and **443 (HTTPS)** — both commonly used for web hosting.  
The scan successfully identified service behavior and supported protocols, completing the task requirements.


