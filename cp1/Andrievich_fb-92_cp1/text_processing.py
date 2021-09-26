def process_text(alphabet):
    with open("text.txt", "r", encoding='1251') as file:
        text = file.read().replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace("ъ", "ь")
        for char in text[:]:
            if char not in alphabet and char != " ":
                text = text.replace(char, "")
        return " ".join(text.split())
