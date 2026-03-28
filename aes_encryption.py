from cryptography.fernet import Fernet

# Generate AES key
def generate_key():
    return Fernet.generate_key()

# Encrypt file
def encrypt_file(filename, key):
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = f.encrypt(data)
    
    with open("encrypted_file.enc", "wb") as file:
        file.write(encrypted_data)

# Decrypt file
def decrypt_file(filename, key):
    f = Fernet(key)
    
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open("decrypted_file.txt", "wb") as file:
        file.write(decrypted_data)