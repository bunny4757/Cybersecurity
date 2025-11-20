# Simulated Security Breach and Audit Log Analysis on Linux

## Objective
The objective of this assignment is to simulate a security breach by executing a harmless “malicious” script on a Linux system and then track its activity using the Linux Audit Framework (auditd). The purpose was to observe file changes and generate audit logs documenting the script’s behavior.

## Tools Used
- Kali Linux virtual machine  
- auditd (Linux auditing system)  
- Bash scripting  

## Steps Followed

### Step 1: Creating a Simulated Malicious Script
A simple malicious-like script was created to simulate unauthorized behavior.  
The script file was created using:

nano malicious.sh
The script performed safe actions such as:

Creating a file

Writing data into it

Creating a directory

After writing the script, execution permissions were added:

 
 
chmod +x malicious.sh
## Step 2: Installing and Enabling Auditd
The auditd service was installed and started to monitor file activity:

```
 
sudo apt update
sudo apt install auditd -y
sudo systemctl start auditd
sudo systemctl enable auditd
Its status was verified with:
systemctl status auditd

```
## Step 3: Adding an Audit Rule to Track File Changes
An audit rule was added to monitor the specific file created by the script:

 
 
sudo auditctl -w /tmp/secret.txt -p rwxa -k malicious_test
This rule monitored:

Read

Write

Execute

Attribute changes

The key malicious_test was used to easily filter logs.

## Step 4: Executing the Script
The simulated malicious script was executed:

 
 
./malicious.sh
This resulted in:

Creation of /tmp/secret.txt

Writing data into the file

Creation of /tmp/hidden_folder

# Step 5: Viewing Audit Logs
Audit logs for the file were retrieved using:
 
sudo ausearch -k malicious_test
This command displayed all logged events related to the simulated malicious activity.

## Step 6: Exporting the Audit Log Output
The audit log entries were saved to a file for documentation:
 
sudo ausearch -k malicious_test > audit_log_report.txt
This file can be used for screenshots or review.


## Screenshots
![1](https://github.com/bunny4757/Cybersecurity/blob/main/Incident%20Response%20and%20Digital%20Forensics/Images/malscript.png)
![1](https://github.com/bunny4757/Cybersecurity/blob/main/Incident%20Response%20and%20Digital%20Forensics/Images/status%20check.png)
![1](https://github.com/bunny4757/Cybersecurity/blob/main/Incident%20Response%20and%20Digital%20Forensics/Images/auditlogs.png)


## Conclusion
This assignment showed how a simulated security breach can be safely recreated using a harmless script.
With the help of auditd, all file changes made by the script were captured and logged.
This demonstrates the value of auditing tools in detecting and analyzing suspicious actions on Linux systems.
