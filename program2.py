import urllib.parse
import pyperclip

if __name__ == "__main__":
    encoded_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"
    
    # Декодування URL
    decoded_url = urllib.parse.unquote(encoded_url)
    
    print("Вхідне посилання:")
    print(encoded_url)
    print("\nДекодоване посилання:")
    print(decoded_url)
    
    # Копіювання в буфер обміну
    try:
        pyperclip.copy(decoded_url)
        print("\n[Успішно] Декодоване посилання скопійовано до буфера обміну операційної системи!")
    except Exception as e:
        print(f"\nПомилка копіювання в буфер обміну: {e}")