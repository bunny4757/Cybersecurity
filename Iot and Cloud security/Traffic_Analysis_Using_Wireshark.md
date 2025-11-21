# IoT Traffic Analysis and Detection of Unsecured Communications
# Objective

The objective of this assignment is to analyze network traffic between two IoT-like devices using a packet capture (PCAP) file.
Using Wireshark, various protocol filters were applied to identify unencrypted or unsecured communications that could expose sensitive information on a network.

# Tools Used

Wireshark (network protocol analyzer)

Pre-captured PCAP file

# Steps Followed
# Step 1: Loading the PCAP File

The PCAP file was opened in Wireshark for inspection.
Wireshark automatically decoded all packets and displayed details such as protocol, source/destination IPs, timestamps, and packet content.

# Step 2: Applying Filters to Identify Unsecured Traffic

To detect unencrypted IoT communication, multiple protocol-based filters were used.

# 1. HTTP Traffic (Unencrypted Web Communication)
```
http
```
This filter showed plain-text HTTP packets, which are not secure because:

Data is readable

No TLS/HTTPS encryption

Sensitive information can be intercepted

HTTP activity indicates unsecured communication between devices or between device and server.

# 2. TCP Stream Analysis (tcp.stream eq 1)
```
tcp.stream eq 1
```

This filter was used to isolate a specific TCP communication stream from the PCAP file.
Wireshark’s TCP stream indexing makes it easy to analyze one conversation at a time.

After applying the filter, the stream was inspected using:

Right-click → Follow → TCP Stream

If the TCP stream content is readable (plain text), it indicates unsecured communication, meaning the data is transmitted without encryption.

# 3. DHCP Traffic (Device Identification Exposure)
```
dhcp
```

DHCP packets revealed:

Device IP assignments

MAC addresses

Vendor identifiers

This information exposes device fingerprinting details, which can help attackers identify IoT devices on the network.

While DHCP is normally unencrypted, it still counts as unsecured communication exposing internal network details.

# 4. ARP Traffic (Network Discovery Information)
```
arp
```


ARP packets showed:

IP-to-MAC mappings

Device discovery communication

ARP has no encryption and can be exploited in attacks such as ARP spoofing.
Thus, ARP traffic is considered part of insecure device-to-device communications.

# 5. DNS Traffic (Plain-text Domain Queries)
```
dns
```

DNS queries revealed:

Domain names requested by devices

Possible cloud endpoints

Application service names

DNS is always unencrypted in basic form, exposing communication patterns and device behavior.

# Summary of Findings

The applied filters revealed multiple forms of unsecured communications in the PCAP file:

HTTP traffic showed clear-text communication without TLS.

TCP streams contained readable data, confirming lack of encryption.

DHCP packets exposed device IP assignments and MAC addresses.

ARP packets revealed network discovery and device mapping details.

DNS traffic was transmitted in clear text, exposing device queries and communication endpoints.

These findings demonstrate that IoT-like devices were communicating without strong security controls, making their traffic vulnerable to interception and analysis.

# Screenshots
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/http.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/tcp.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/dhcp.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/arp.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/dns.png)
![](https://github.com/bunny4757/Cybersecurity/blob/main/Iot%20and%20Cloud%20security/Images/httpget.png)

# Conclusion

By filtering traffic using HTTP, TCP, DHCP, ARP, and DNS protocols, it was possible to detect several forms of unencrypted and unsecured communication within the PCAP file.
Wireshark clearly showed that sensitive metadata and device information were transmitted in plain text, making the communication vulnerable. This assignment demonstrates how insecure IoT traffic can be identified and analyzed using Wireshark.
