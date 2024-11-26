def rail_fence_cipher(text, key, mode='encrypt'):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    if mode == 'encrypt':
        dir_down = False
        row, col = 0, 0
        
        for char in text:
            if row == 0 or row == key - 1:
                dir_down = not dir_down
            
            rail[row][col] = char
            col += 1
            
            row += 1 if dir_down else -1
        
        return ''.join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])
    
    elif mode == 'decrypt':
        dir_down = None
        row, col = 0, 0
        
        for _ in range(len(text)):
            if row == 0:
                dir_down = True
            elif row == key - 1:
                dir_down = False
            
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1
        
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1
        
        result = []
        row, col = 0, 0
        for _ in range(len(text)):
            if row == 0:
                dir_down = True
            elif row == key - 1:
                dir_down = False
            
            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1
            
            row += 1 if dir_down else -1
        
        return ''.join(result)

def main():
    print("Rail Fence Cipher: Encryption and Decryption")
    
    choice = input("Choose an option (encrypt/decrypt): ").lower()
    text = input("Enter the text: ")
    key = int(input("Enter the key value: "))
    
    if choice in ["encrypt", "decrypt"]:
        result_text = rail_fence_cipher(text, key, mode=choice)
        print(f"{choice.capitalize()}ed text: {result_text}")
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

