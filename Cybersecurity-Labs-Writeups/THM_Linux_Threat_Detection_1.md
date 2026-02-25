# TryHackMe – Linux Threat Detection 1 Writeup

## Platform
TryHackMe

## Room
Linux Threat Detection 1

## Overview
This room focuses on detecting Initial Access techniques in Linux systems.  
The investigation covers SSH abuse, brute-force detection, service exploitation, command injection, and process tree analysis using audit logs.

---

## Task 2 – Initial Access via SSH

#### Q1: When did the Ubuntu user log in via SSH for the first time?
Command used:
```
bash
cat /var/log/auth.log | grep sshd
```
Answer:

2024-10-22




#### Q2: Did the Ubuntu user use SSH keys instead of a password?

Log analysis showed:

Accepted publickey for ubuntu

Answer:

Yea

 

## Task 3 – Detecting SSH Attacks
#### Q1: When did the SSH password brute force start?

Command used:
```
cat /var/log/auth.log | grep password
```
Answer:

2025-08-21

 


#### Q2: Which four users did the botnet attempt to breach?

Answer:

root, roy, sol, user

 


#### Q3: Which IP managed to breach the root user?

Command used:
```
cat /var/log/auth.log | grep Accepted
```
Answer:

91.224.92.79

 


## Task 4 – Initial Access via Services2
#### Q1: What is the path to the Python file the attacker attempted to open?

Answer:

/opt/trypingme/main.py

 


#### Q2: What flag was inside the file?

Answer:

THM{i_am_vulnerable!}

 


## Task 5 – Detecting Service Breach
#### Q1: What is the PPID of the suspicious whoami command?

Command used:
```
ausearch -i -x whoami
```
Answer:

1018

 


#### Q2: What is the PID of the TryPingMe app?

Answer:

577

 

#### Q3: Which program was used to open the reverse shell?

Answer:

Python

 


## Task 6 – Advanced Initial Access
#### Q1: Which Initial Access technique is likely used if a trusted app suddenly runs malicious commands?

Answer:

Supply Chain Compromise
#### Q2: Which detection method can detect various Initial Access techniques?

Answer:

Process Tree Analysis

## Screenshots
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_1.png)
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_2.png)
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_3.png)
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_4.png)
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_5.png)
![SSH Login](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/try_linux_detec_tk_6.png)

## Conclusion

This room demonstrated how attackers gain access to Linux systems through SSH exposure, brute-force attacks, and vulnerable services. By analyzing authentication logs, web logs, and auditd process trees, it was possible to trace malicious activity back to its origin.

The lab strengthened practical skills in:

SSH log investigation

Brute-force detection

Command injection analysis

Process tree building

Incident investigation in Linux environments

### Reference

Room completed on TryHackMe
Room Name: Linux Threat Detection 1
