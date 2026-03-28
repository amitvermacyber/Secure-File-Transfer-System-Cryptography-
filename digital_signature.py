from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

def sign_file(filename):
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

    with open(filename, "rb") as f:
        data = f.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    with open("signature.sig", "wb") as f:
        f.write(signature)

def verify_signature(filename):
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

    with open(filename, "rb") as f:
        data = f.read()

    with open("signature.sig", "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Signature Verified ✅")
    except:
        print("Signature Invalid ❌")