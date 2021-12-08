def process_text(alphabet, file_with_text):
    with open(file_with_text, "r", encoding='utf8') as file:
        text = file.read().replace("\n", " ").replace("\r", "").lower().replace("ё", "е").replace("ъ", "ь")
        for char in text[:]:
            if char not in alphabet and char != " ":
                text = text.replace(char, "")
        return "".join(text.split())
