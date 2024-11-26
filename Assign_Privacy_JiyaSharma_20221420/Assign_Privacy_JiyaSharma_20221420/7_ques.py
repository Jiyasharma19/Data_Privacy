import hashlib
import rsa

# Generate RSA keys
def generate_keys():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

# Digitally sign a document
def sign_document(document, private_key):
    # Hash the document using SHA-256
    document_hash = hashlib.sha256(document.encode('utf-8')).digest()
    # Sign the hash using the private key
    signature = rsa.sign(document_hash, private_key, 'SHA-256')
    return signature

# Verify the signature of a document
def verify_signature(document, signature, public_key):
    try:
        # Hash the document using SHA-256
        document_hash = hashlib.sha256(document.encode('utf-8')).digest()
        # Verify the signature using the public key
        rsa.verify(document_hash, signature, public_key)
        return True
    except rsa.VerificationError:
        return False

def main():
    # Generate public and private keys
    public_key, private_key = generate_keys()

    # Original document
    document = "This is a confidential document."
    
    # Sign the document
    signature = sign_document(document, private_key)
    print("Document signed successfully.")
    
    # Send the document and signature (simulation)
    print("Sending document and signature...")
    
    # Receiver verifies the document
    is_valid = verify_signature(document, signature, public_key)
    if is_valid:
        print("The document is verified successfully. The signature is valid.")
    else:
        print("The document verification failed. The signature is invalid.")

if __name__ == "__main__":
    main()

