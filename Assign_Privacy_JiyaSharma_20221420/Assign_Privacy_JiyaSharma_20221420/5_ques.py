import random

# Function to generate a random password using words from a dictionary file
def generate_password(dictionary_file_path, word_count=4, delimiter=''):
    try:
        # Read words from the dictionary file
        with open(dictionary_file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
            
        # Ensure the dictionary contains enough words
        if len(words) < word_count:
            raise ValueError("The dictionary file doesn't contain enough words.")
        
        # Select random words and form the password
        password_words = random.sample(words, word_count)
        password = delimiter.join(password_words)
        return password
    except FileNotFoundError:
        print("Error: The specified dictionary file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to generate and print the password
def main():
    dictionary_file_path = "dictionary.txt"
    password = generate_password(dictionary_file_path, word_count=4, delimiter='-')
    if password:
        print("\n")
        print("\n")

        print("Generated Password:", password)
        print("\n")
        print("\n")


if __name__ == "__main__":
    main()

