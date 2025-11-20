#  Analysis of Suspicious Login Attempts Using Splunk
# Objective

The objective of this assignment is to analyze authentication-related log data using Splunk to identify suspicious login attempts. The goal was to extract timestamps, source IP addresses, and any patterns that indicate unauthorized access activity.

# Tools Used

Splunk (log indexing & search)

Authentication log file uploaded to Splunk

Splunk SPL (Search Processing Language)

# Log Source

A previously collected log file was uploaded into Splunk.
This log contained:

Failed login attempts

Invalid user login attempts

Authentication errors

Source IP addresses

Timestamps

This file was used as an alternative to /var/log/auth.log, since Kali Linux did not generate SSH logs due to SSH being disabled.

# Steps Followed
# Step 1 — Uploading Log File to Splunk

The authentication log file was uploaded into Splunk using:

Add Data → Upload File → Index → Search

Splunk automatically parsed timestamps and fields.

# Step 2 — Searching for Failed Login Attempts

A Splunk SPL query was executed to filter authentication failures, such as:

Invalid username attempts

Failed password attempts

Authentication errors

This allowed identification of suspicious login events inside Splunk’s search interface.

Example events seen in Splunk search results:

“authentication failed”

“invalid user”

“failed login attempt”

# Step 3 — Extracting Timestamps and IP Addresses

Splunk automatically extracted key fields such as:

_time (timestamp)

src, source_ip, or client_ip (depending on the log format)

These fields were used to identify when and from where suspicious login attempts occurred.

Patterns observed included:

Multiple failed logins from the same IP

Repeated rapid attempts

Attempts using unknown or invalid users

# Step 4 — Identifying Suspicious Activity

Based on the Splunk search results, suspicious activity included:

Several failed login attempts within seconds

Repeated failures from the same IP address

Invalid user login attempts (possible brute-force activity)

These behaviors often indicate:

Credential guessing

Unauthorized access attempts

Automated brute-force tools

# Summary of Findings

Splunk revealed multiple failed login attempts.

Several events originated from the same IP, indicating possible brute-force activity.

Timestamps and IPs were clearly visible through Splunk’s extracted fields.

# Screenshots
![](https://github.com/bunny4757/Cybersecurity/blob/main/Incident%20Response%20and%20Digital%20Forensics/Images/failedloginattempts.png)
# Conclusion

Using Splunk, it was possible to analyze authentication logs effectively and detect suspicious login attempts. Splunk’s field extraction and search capabilities made it easy to identify timestamps, IP addresses, and repeated failed login activities. This assignment demonstrates how SIEM tools like Splunk assist in identifying potential security breaches and unauthorized access attempts.
