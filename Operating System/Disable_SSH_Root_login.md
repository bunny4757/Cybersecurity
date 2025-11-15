# Disable SSH Root Login on Linux

## Objective
The goal of this assignment is to improve the security of a Linux system by disabling SSH root login.  
After editing the SSH configuration file, the SSH service is restarted and the change is verified by attempting a remote root login.

---

## Step-by-Step Procedure

### Step 1 — Open the SSH Configuration File
Use the following command to edit the SSH configuration file:

sudo nano /etc/ssh/sshd_config

 
 

This file controls all SSH-related settings on the system.

---

### Step 2 — Locate the Root Login Line
Find the following line:

#PermitRootLogin prohibit-password

 
 

This line may vary depending on the Linux distribution. It is usually commented out (`#` at the beginning).

---

### Step 3 — Disable SSH Root Login
Modify the line to:

PermitRootLogin no

 
 

Explanation:
- `PermitRootLogin no` → Completely blocks SSH login for the root user.
- This prevents attackers from trying to brute-force the root password over SSH.

Save and exit nano:
- Press **CTRL + O** → Save  
- Press **Enter**  
- Press **CTRL + X** → Exit  

---

### Step 4 — Restart the SSH Service
Apply the changes by restarting the SSH daemon:

sudo systemctl restart ssh

nginx
 

or depending on your system:

sudo systemctl restart sshd

 
 

If no errors appear, SSH restarted successfully.

---

### Step 5 — Verify That Root Login Is Disabled
Attempt to log in as root using SSH:

ssh root@localhost

 
 

Expected output:

Permission denied

 
 

This confirms that SSH root login has been successfully disabled.

---

## 📸 Screenshots to Include

---

## Understanding Why This Is Important

SSH allows remote access to a Linux system. Allowing root login is a major security risk because:
- Root has unlimited power  
- Attackers often target root accounts  
- Brute-force attacks become easier  

By disabling root login:
- Only normal users can access the system via SSH  
- Normal users must use `sudo` to get admin privileges  
- This protects the system from unauthorized access  

---

## 🏁 Conclusion

In this, we configured the Linux SSH daemon to block root login, enhanced system security, and verified the changes by testing SSH authentication. Disabling SSH root login is a standard security practice used by system administrators to reduce attack surfaces and prevent unauthorized access to critical systems.

