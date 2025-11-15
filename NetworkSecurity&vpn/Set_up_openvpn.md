# Set Up OpenVPN on Linux and Verify IP Address

## Objective
The purpose of this assignment is to install and configure OpenVPN on a Linux machine, connect to a VPN using an OpenVPN configuration file, and verify the change in public IP address before and after connecting to the VPN.

---

## Step-by-Step Procedure

### Step 1 — Update System Packages
Update all system packages to ensure the latest versions are installed:

sudo apt update && sudo apt upgrade -y

 
 

---

### Step 2 — Install OpenVPN
Install OpenVPN using:

sudo apt install openvpn -y

 
 

This installs the OpenVPN client required to connect to VPN servers.

---

### Step 3 — Check Public IP Before Connecting
Run the following command to display your current public IP:

curl ifconfig.me

 
 

 Save this IP address — it will be different after connecting to VPN.

---

### Step 4 — Get an OpenVPN Configuration File (.ovpn)
To connect to a VPN, you need a valid `.ovpn` configuration file.

You can download free OpenVPN configs from:

- **VPNBook** → https://www.vpnbook.com/freevpn (No signup required)  
- **ProtonVPN (Free)** → OpenVPN configs (Signup required)

Download and extract the `.ovpn` file you want to use.

Move it to your working directory:

cp ~/Downloads/yourfile.ovpn .

 
 

---

### Step 5 — Connect to the VPN

Run:

sudo openvpn --config yourfile.ovpn

csharp
 

If using VPNBook, enter the username & password displayed on their website.

Successful connection will show:

Initialization Sequence Completed

 
 

---

### Step 6 — Verify IP After Connecting
Open a new terminal (keep the VPN terminal running) and run:

curl ifconfig.me

 
 

You should now see a **different IP** — the VPN server’s IP.

This confirms the VPN connection is working correctly.

---

###  Step 7 — Disconnect from VPN
Press:

CTRL + C

 
 

You should see:

SIGINT received, exiting

 
 

This stops the VPN tunnel.

---

## Screenshots to Include

![hostip](https://github.com/bunny4757/Cybersecurity/blob/main/NetworkSecurity%26vpn/images/ipaddr.png)
![ovpnip](https://github.com/bunny4757/Cybersecurity/blob/main/NetworkSecurity%26vpn/images/ovpn.png)
![newip](https://github.com/bunny4757/Cybersecurity/blob/main/NetworkSecurity%26vpn/images/newip.png)
 
 

---

## Understanding This Assignment

OpenVPN is one of the most widely used VPN protocols for secure remote communication.  
When connected:

- Your traffic is encrypted  
- Your IP address is masked  
- Your connection appears to come from the VPN server  

Verifying your public IP before and after ensures the VPN tunnel is active and functioning.

---

## Conclusion

In this assignment, OpenVPN was successfully installed and configured on a Linux machine.  
A VPN connection was established using a valid `.ovpn` file, and the public IP address was verified before and after connecting.  
This demonstrates an understanding of VPN tunneling, OpenVPN configuration, and network identity masking.


