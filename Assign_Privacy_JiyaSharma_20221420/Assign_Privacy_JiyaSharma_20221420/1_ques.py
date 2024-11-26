def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift_amount = shift % 26
    
    if mode == 'decrypt':
        shift_amount = -shift_amount

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher: Encryption and Decryption")
    
    choice = input("Choose an option (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    if choice in ["encrypt", "decrypt"]:
        result_text = caesar_cipher(text, shift, mode=choice)
        print(f"{choice.capitalize()}ed text: {result_text}")
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

