# TryHackMe – ContAInment Writeup

## Category
Blue Team / Incident Response  

---

## Scenario

In this challenge, we act as a **Security Analyst at West Tech**, where unusual activity was detected on an employee workstation. A ransom note indicated that sensitive data had been exfiltrated and encrypted.

**Objective:**
- Investigate the incident  
- Trace attacker activity  
- Recover encrypted data  
- Identify the flag  

---

## Initial Access

SSH access was provided:

```bash
ssh o.deer@<Machine_IP>
```

---

## Reconnaissance

To begin the investigation, I searched for packet capture files:

```bash
find /home/o.deer/ -type f -name "*.pcap"
```

### Observation

Multiple `.pcap` files were found across directories.  
By analyzing file sizes, one file stood out as an outlier:

```
session_4444_dump.pcap
```

---

## PCAP Analysis

Using the provided AI assistant, I reassembled the suspicious `.pcap` file:

```
Reassemble /home/o.deer/Documents/pcap_dumps/2025-06-17/session_4444_dump.pcap
```

### Output File

```
/home/o.deer/qwen-output/reassembled_data_dump.txt
```

---

## Key Findings

From the reconstructed data:

- Evidence of **prompt injection attack**
- Internal data leakage through AI manipulation  
- Attacker notes revealed a critical string:

```
westtechvictim1
```

This was identified as a **password for the encrypted archive**.

---

## Encrypted File Analysis

Located file:

```
/home/o.deer/westtech_projects_encrypted.zip
```

### Extraction

```bash
unzip westtech_projects_encrypted.zip -d /dev/shm/
```

Password used:

```
westtechvictim1
```

### Extracted Files

- thm_flags.txt  
- thm_flags_guide.txt  
- project documents and logs  

---

## Flag Analysis

The file `thm_flags.txt` contained multiple Base64 encoded entries:

```bash
head thm_flags.txt
```

Example:

```
dGhtezUyLDY1LDE3LDk1LDE0fQ==
```

Using the provided logic (via tool or manual analysis), the valid flag was identified based on the challenge conditions.

---

## Final Flag

```
THM{23,82,20,17,53}
```


---
## Screenshots

![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment1.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment2.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment3.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment4.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment5.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/THM_contaiment6.png)



---


## Conclusion

This challenge demonstrated:

- Incident response workflow  
- Network traffic analysis using PCAP files  
- Prompt injection risks in AI systems  
- Data exfiltration investigation  
- Handling encrypted data and decoding techniques  

It highlights how **AI misuse and weak data handling** can lead to serious security incidents.

---



