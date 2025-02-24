def word_counter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()  
        
        words = text.split()
        word_count = {}

        for word in words:
            word = word.strip(".,!?()[]{}:;\"'") 
            word_count[word] = word_count.get(word, 0) + 1  

        # Display results
        print("\nWord Frequency Count:")
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")


file_path = "test.txt"  
word_counter(file_path)
