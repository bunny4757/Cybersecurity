# BTLO – Shiba Insider Challenge Writeup

## Platform
Blue Team Labs Online (BTLO)

## Challenge Name
Shiba Insider

---

## Objective
The goal of this challenge was to investigate provided evidence files and identify an insider.  
The investigation involved packet analysis, credential extraction, metadata analysis, steganography, and OSINT techniques.

---

## Files Provided
- PCAP file
- Password-protected ZIP file

---

## Tools Used
- Wireshark
- ExifTool
- Steghide
- Web Browser (OSINT)

---

## Investigation Process

### Step 1 — PCAP Analysis

The PCAP file was opened in Wireshark.  
A short client-server conversation was observed.

From the traffic:
- Client request: “how do I open file”
- Server response: “use your own password”

#### Answer: use your own password


Screenshots:
![1](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_1.png)

---

### Step 2 — Extract ZIP Password

While inspecting the HTTP Authorization header in the PCAP file, credentials were identified.

The encoded credentials revealed the password for the ZIP file.

#### Answer: redforever


Screenshots:
![2](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_2.png)

---

### Step 3 — Additional Password Requirement

After extracting the ZIP file using the password `redforever`, the archive contained:
- A text file
- An image file

The text file clearly stated that no further passwords were required

#### Answer: No


---

### Step 4 — Metadata Analysis

The image file was analyzed using ExifTool:

```bash
exiftool image.jpg
```
The metadata revealed an interesting technique used within the image.

### Answer:Technique: Steganography

Screenshots:

![3](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_3.png)

### Step 5 — Extract Hidden Data

Since steganography was identified, Steghide was used to extract hidden content:
```
steghide extract -sf image.jpg
```
This revealed a hidden ID.

#### Answer:0726ba878ea47de571777a

Screenshots:

![4](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_4.png)

### Step 6 — Identify the Insider

The extracted ID was used to locate the attacker profile within the BTLO platform.

By replacing the user ID in the BTLO profile URL with the extracted ID, the insider's profile was discovered.

#### Answer:bluetiger

Screenshots:

![6](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_6.png)
![5](https://github.com/bunny4757/Cybersecurity/blob/main/Cybersecurity-Labs-Writeups/Images/btlo_df_5.png)

### Key Learnings

Basic packet inspection using Wireshark

Extracting credentials from HTTP Authorization headers

Metadata analysis using ExifTool

Steganography detection and extraction

Using OSINT techniques to identify user profiles

Importance of analyzing small details in investigations

### Conclusion

The Shiba Insider challenge demonstrated how multiple small investigative techniques combine to uncover hidden information.
By analyzing network traffic, extracting embedded credentials, inspecting image metadata, and retrieving hidden data through steganography, the insider was successfully identified.

This lab reinforced practical blue team skills including traffic analysis, file inspection, and digital investigation workflows.


### Reference

Challenge completed on Blue Team Labs Online (BTLO)
Challenge Name: Shiba Insider


---
