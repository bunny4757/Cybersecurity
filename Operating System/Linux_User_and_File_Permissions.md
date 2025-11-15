# Linux Users and File Permissions

## 📌 Objective
Create two user accounts in Linux.  
Create a file that only one user (user1) can read and write,  
and ensure the other user (user2) has no access to it.

---

## 🧭 Step-by-Step Commands (Easy and Complete)

### 👉 Step 1 — Create Two Users
Run these commands in the terminal:

sudo adduser user1
sudo adduser user2

This creates two separate user accounts.

---

### 👉 Step 2 — Switch to user1

su - user1

 
 

Now you are logged in as **user1**.

---

### 👉 Step 3 — Create a File as user1

touch secretfile.txt
echo "This file belongs to user1 only." > secretfile.txt

sql
 

Check permissions:

ls -l secretfile.txt


---

### 👉 Step 4 — Give Access ONLY to user1

Use chmod:

chmod 600 secretfile.txt

markdown
 

Explanation of `600`:
- **6** = read + write for the owner (user1)  
- **0** = no permissions for group  
- **0** = no permissions for others  

Check again:

ls -l secretfile.txt

 
 

You should see:

-rw------- 1 user1 user1 secretfile.txt

 
 

This means:
- user1 → read + write  
- user2 → NO access  
- others → NO access  

---

### 👉 Step 5 — Switch to user2 and Test

su - user2

powershell
 

Try reading user1’s file:

cat /home/user1/secretfile.txt

makefile
 

Expected:

cat: /home/user1/secretfile.txt: Permission denied

Try writing:

echo "test" >> /home/user1/secretfile.txt

Again:

Permission denied

This proves the permissions are correct.

---

