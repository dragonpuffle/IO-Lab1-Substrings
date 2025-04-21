
#--------FILE UTILS-----------------------------------

def read_file(filename: str) -> str:
    text = None
    with open(filename, mode="r") as f:
        text = f.read()
        return text

#-------MAIN ALGORITHMS--------------------------------

def naive_algorithm(substring: str, main_text: str) -> int:
    substr_len = len(substring)
    main_text_len = len(main_text)
    if substr_len == 0 or main_text_len == 0:
        return -1
    for i in range(main_text_len):
        if i + substr_len > main_text_len:
            return -1
        if substring == main_text[i:i + substr_len]:
            return i


if __name__ == "__main__":
    # Naive algorithm
    substring = read_file("substr.txt")
    text = read_file("test.txt")
    print(f"Substring: {substring}\nText: {text}\n")
    pos = naive_algorithm(substring, text)
    print(f"Position of substring: {pos}")
    if pos > 0:
        print(f"\nText started with substring: {text[pos:]}")

