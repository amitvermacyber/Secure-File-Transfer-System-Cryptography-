from aes_encryption import generate_key, encrypt_file, decrypt_file
from rsa_encryption import encrypt_key, decrypt_key
from digital_signature import sign_file, verify_signature

print("🔥 MAIN FILE IS RUNNING")

print("🔑 Generating AES key...")
aes_key = generate_key()

print("🔐 Encrypting file...")
encrypt_file("testfile.txt", aes_key)

print("🔑 Encrypting AES key with RSA...")
encrypt_key(aes_key)

print("✍️ Signing file...")
sign_file("encrypted_file.enc")

print("📤 File encrypted and signed!")

# -------- Receiver Side --------

print("📥 Decrypting AES key...")
decrypted_key = decrypt_key()

print("🔓 Decrypting file...")
decrypt_file("encrypted_file.enc", decrypted_key)

print("✅ Verifying signature...")
verify_signature("encrypted_file.enc")