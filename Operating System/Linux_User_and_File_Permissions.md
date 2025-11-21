# Linux Users and File Permissions

## Objective
Create two user accounts in Linux.  
Create a file that only one user (user1) can read and write,  
and ensure the other user (user2) has no access to it.

---

## Step-by-Step Commands

###  Step 1 — Create Two Users
Run these commands in the terminal:
```
sudo adduser user1
sudo adduser user2
```
This creates two separate user accounts.



###  Step 2 — Switch to user1
```
su - user1
```
 
 

Now you are logged in as **user1**.

---

###  Step 3 — Create a File as user1
```
touch secretfile.txt
echo "This file belongs to user1 only." > secretfile.txt
```

 

Check permissions:
```
ls -l secretfile.txt
```

---

###  Step 4 — Give Access ONLY to user1

Use chmod:
```
chmod 600 secretfile.txt
```
markdown
 

Explanation of `600`:
- **6** = read + write for the owner (user1)  
- **0** = no permissions for group  
- **0** = no permissions for others  

Check again:
```
ls -l secretfile.txt
```
 
 

You should see:

-rw------- 1 user1 user1 secretfile.txt

 
 

This means:
- user1 → read + write  
- user2 → NO access  
- others → NO access  

---

###  Step 5 — Switch to user2 and Test
```
su - user2
```

Try reading user1’s file:
```
cat /home/user1/secretfile.txt
```
makefile
 

Expected:

cat: /home/user1/secretfile.txt: Permission denied

Try writing:

echo "test" >> /home/user1/secretfile.txt

Again:

Permission denied

This proves the permissions are correct.

---

## Screenshots

![user1 file creation](https://github.com/bunny4757/Cybersecurity/blob/main/Operating%20System/Images/user1.png)

![chnange permissions](https://github.com/bunny4757/Cybersecurity/blob/main/Operating%20System/Images/chmoduser1.png)

![user2 denied](https://github.com/bunny4757/Cybersecurity/blob/main/Operating%20System/Images/user2denied.png)


## Conclusion

In this assignment, we successfully created two separate user accounts in Linux and configured file permissions to ensure secure access control. By using the `chmod 600` permission mode, we restricted the file so that only the owner (user1) could read and write to it, while user2 had no access at all. This demonstrates how Linux file permissions protect sensitive data and enforce user-level security. Overall, the task helped in understanding user management, file ownership, and permission settings—fundamental concepts in system administration and cybersecurity.

