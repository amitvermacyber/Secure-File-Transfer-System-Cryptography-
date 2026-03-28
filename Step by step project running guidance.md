\##############################################################**STEP BY STEP GUIDANCE**##########################################################################



**🚀 🔐 Step-by-Step Project Running Guide**



**🧩 Step 1: Open Project Folder**



**🐍 Step 2: Install Required Library**



Run:



py -m pip install cryptography



👉 This installs the required cryptography package



**📁 Step 3: Check Required Files**



Make sure your folder contains:



key\_generation.py



aes\_encryption.py



rsa\_encryption.py



digital\_signature.py



main.py



testfile.txt



**✍️ Step 4: Add Content to File**



Open testfile.txt and write:



This is a secure file transfer test.



**🔑 Step 5: Generate RSA Keys**



Run:



py key\_generation.py



**👉 Output:**



Keys generated successfully!



✔ Creates:



private\_key.pem



public\_key.pem



**▶️ Step 6: Run Main Program**



Run:



py main.py



**✅ Step 7: Expected Output**



You should see:



🔑 Generating AES key...

🔐 Encrypting file...

🔑 Encrypting AES key with RSA...

✍️ Signing file...

📤 File encrypted and signed!

📥 Decrypting AES key...

🔓 Decrypting file...

✅ Verifying signature...

Signature Verified ✅



**📂 Step 8: Check Output Files**



After running, these files will be created:



encrypted\_file.enc 🔐



encrypted\_key.bin 🔑



signature.sig ✍️



decrypted\_file.txt 📄



**🔍 Step 9: Verify Results**



Open:



👉 decrypted\_file.txt



✔ It should contain the same content as testfile.txt



**🧪 Step 10: Test Security (Important)**



Try this:



Open encrypted\_file.enc

Modify some content

Run program again



👉 Output should show:



Signature Invalid ❌



✔ This proves integrity protection works

