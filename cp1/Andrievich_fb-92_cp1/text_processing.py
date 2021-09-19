def process_text(alphabet):
    with open("text_2.txt", "r", encoding='utf8') as file:
        text = file.read().replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace("ъ", "ь")
        for char in text[:]:
            if char not in alphabet and char != " ":
                text = text.replace(char, "")
        return " ".join(text.split())
