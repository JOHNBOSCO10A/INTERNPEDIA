import string

def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split text into words and count
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Count Tool!")
    while True:
        print("Select input method:")
        print("1. Input text directly")
        print("2. Read from file")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ")
        
        if choice == '1':
            text = input("Enter text: ")
            if text.strip() == '':
                print("Error: Empty text!")
            else:
                print("Word count:", count_words(text))
        
        elif choice == '2':
            filename = input("Enter filename: ")
            try:
                with open(filename, 'r') as file:
                    text = file.read()
                    print("Word count:", count_words(text))
            except FileNotFoundError:
                print("Error: File not found!")
        
        elif choice == '3':
            print("Farewell! Thanks for using the Word Count Tool.")
            break
        
        else:
            print("Error: Invalid choice!")

if __name__ == "__main__":
    main()
