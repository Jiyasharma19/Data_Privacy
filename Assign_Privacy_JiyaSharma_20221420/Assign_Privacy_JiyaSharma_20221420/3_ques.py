import hashlib

# Function to hash a password using SHA-256
def hash_password(password, algorithm='sha256'):
    try:
        hash_function = hashlib.new(algorithm)
    except ValueError:
        raise ValueError("Unsupported hashing algorithm. Use 'sha256', 'sha512', etc.")
    
    # Update the hash object with the password encoded to bytes
    hash_function.update(password.encode('utf-8'))
    
    # Return the hexadecimal representation of the hash
    return hash_function.hexdigest()

def main():
    print("Password Hashing with SHA-256")
    
    password = input("Enter the password: ")
    hashed_password = hash_password(password)
    print("SHA-256 Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()

