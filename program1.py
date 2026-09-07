import re

def custom_sort(words):
    def sort_key(word):
        clean_word = word.strip('.,!?"\'()[]{}').lower()
        if not clean_word:
            return (2, word)
        # Українські літери спочатку (група 0)
        if re.match(r'^[а-яіїєґ]', clean_word):
            return (0, clean_word)
        # Латинські літери потім (група 1)
        elif re.match(r'^[a-z]', clean_word):
            return (1, clean_word)
        # Інші символи
        else:
            return (2, clean_word)
            
    return sorted(words, key=sort_key)

if __name__ == "__main__":
    try:
        with open("text_data.txt", "r", encoding="utf-8") as file:
            text = file.read()
            
        print("--- Вхідний текст ---")
        print(text)
        print("-" * 30)
        
        words = text.split()
        sorted_words = custom_sort(words)
        
        print("\n--- Відсортований список слів ---")
        print(sorted_words)
    except FileNotFoundError:
        print("Файл text_data.txt не знайдено.")
