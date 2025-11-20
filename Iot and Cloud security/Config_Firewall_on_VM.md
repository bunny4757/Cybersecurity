# Configure Firewall to Allow Only HTTP and SSH on a Virtual Machine
# Objective

The objective of this assignment is to configure a firewall on a virtual machine so that only SSH (port 22) and HTTP (port 80) are allowed. All other incoming ports must remain blocked. The configuration was done on a Linux virtual machine running in VMware using the UFW firewall.

# Tools Used

VMware Workstation (Virtual Machine)

Kali Linux (Guest OS)

UFW (Uncomplicated Firewall)

Nmap (Port scanning for verification)

# Steps Followed
# Step 1 – Enable the Firewall

UFW was enabled on the Kali Linux VM using:

sudo ufw enable


This activated the firewall and set it to start automatically on system boot.

# Step 2 – Allow SSH and HTTP Ports

Only SSH and HTTP services were allowed:

sudo ufw allow 22
sudo ufw allow 80


These rules allow secure shell access (port 22) and web traffic (port 80).

# Step 3 – Set Default Firewall Policy

The default policy was configured to block all other incoming connections:

sudo ufw default deny incoming
sudo ufw default allow outgoing


This ensures that:

Only ports explicitly allowed remain open.

All other ports are denied.

# Step 4 – Verify Active Firewall Rules

The current firewall status was checked with:

sudo ufw status verbose


Expected output included:

22/tcp ALLOW IN Anywhere
80/tcp ALLOW IN Anywhere


All other ports were shown as blocked.

# Step 5 – Verify Ports Using Nmap

An Nmap scan was performed from the host system (Windows) against the VM’s IP address:

nmap -Pn <VM-IP>


The results showed:

22/tcp open ssh
80/tcp open http
All other scanned ports: closed | filtered


This confirmed that only SSH and HTTP ports were accessible, and all other ports were blocked by the firewall.

# Summary of Findings

The firewall (UFW) was enabled and configured successfully.

Only ports 22 (SSH) and 80 (HTTP) were allowed.

All other ports were blocked by default.

Nmap verification confirmed that the VM only exposes these two ports.

The firewall rules behaved exactly as expected.

# Screenshots

![1](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/ufwstatus.png)
![2](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/ufwresult.png)

# Conclusion

This assignment demonstrated how to configure and verify firewall rules on a Linux virtual machine. By allowing only essential ports (SSH and HTTP) and blocking all others, the system’s security posture is significantly improved. The verification using Nmap confirms that the firewall configuration works as intended.
