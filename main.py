
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

def make_bias_table(substring: str)->dict:
    substring_len = len(substring)
    bias_table = {"END": substring_len}
    for i in range(1, substring_len):
        if substring[substring_len - 1 - i] not in bias_table.keys():
            bias_table[substring[substring_len - 1 - i]] = i
    if substring[substring_len - 1] not in bias_table.keys():
        bias_table[substring[substring_len - 1]] = substring_len
    return bias_table

def Boyer_Moore_Horspool_algorithm(substring: str, main_text: str) -> int:
    substr_len = len(substring)
    main_text_len = len(main_text)
    if substr_len == 0 or main_text_len == 0:
        return -1
    bias_table = make_bias_table(substring)
    index = 0
    while index + substr_len < main_text_len:
        flag = True
        for i in range(substr_len):
            if substring[substr_len - 1 - i] != main_text[index + substr_len - 1 - i]:
                if i == 0:
                    if main_text[index + substr_len - 1 - i] in bias_table.keys():
                        index += bias_table[main_text[index + substr_len - 1 - i]]
                    else:
                        index += bias_table["END"]
                else:
                    index += bias_table[substring[substr_len - 1]]
                flag = False
                break
        if flag:
            return index
    return -1

if __name__ == "__main__":
    # Substring and text
    substring = read_file("substr.txt")
    text = read_file("test.txt")
    print(f"Substring: {substring}\nText: {text}")
    # Naive algorithm
    print("\n-----Naive algorithm-----")
    pos = naive_algorithm(substring, text)
    print(f"Position of substring: {pos}")
    if pos > 0:
        print(f"\nText started with substring: {text[pos:]}")

    # Boyer-Moore-Horspool algorithm
    print("\n-----Boyer-Moore-Horspool algorithm-----")
    pos = Boyer_Moore_Horspool_algorithm(substring, text)
    print(f"Position of substring: {pos}")
    if pos > 0:
        print(f"\nText started with substring: {text[pos:]}")

