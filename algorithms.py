# --------FILE UTILS-----------------------------------

def read_file(filename: str) -> str:
    text = None
    with open(filename, mode="r", encoding='utf-8') as f:
        text = f.read()
        return text


# --------OPERATIONS COUNTER---------------------------

operation_counter = 0

def reset_counter():
    global operation_counter
    operation_counter = 0

def increment_counter(n: int = 1):
    global operation_counter
    operation_counter += n

def get_counter():
    return operation_counter


# -------MAIN ALGORITHMS--------------------------------

# Naive algorithm
def naive_algorithm(substring: str, main_text: str) -> int:
    reset_counter()
    substr_len = len(substring)
    main_text_len = len(main_text)
    if substr_len == 0 or main_text_len == 0:
        return -1
    for i in range(main_text_len):
        if i + substr_len > main_text_len:
            return -1
        increment_counter(substr_len)
        if substring == main_text[i:i + substr_len]:
            return i

    return -1


# Boyer-Moore-Horspool algorithm
def make_bias_table(substring: str) -> dict:
    substring_len = len(substring)
    bias_table = {"END": substring_len}
    for i in range(1, substring_len):
        if substring[substring_len - 1 - i] not in bias_table.keys():
            bias_table[substring[substring_len - 1 - i]] = i
    if substring[substring_len - 1] not in bias_table.keys():
        bias_table[substring[substring_len - 1]] = substring_len
    return bias_table


def Boyer_Moore_Horspool_algorithm(substring: str, main_text: str) -> int:
    reset_counter()
    substr_len = len(substring)
    main_text_len = len(main_text)
    if substr_len == 0 or main_text_len == 0:
        return -1
    bias_table = make_bias_table(substring)
    index = 0
    while index + substr_len - 1 < main_text_len:
        flag = True
        for i in range(substr_len):
            increment_counter()
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


# Knuth–Morris–Pratt algorithm
def make_prefix(substring: str) -> list:
    substr_len = len(substring)
    prefix_arr = [0] * substr_len
    for i in range(1, substr_len):
        current_prefix = prefix_arr[i - 1]
        increment_counter()
        while current_prefix > 0 and substring[current_prefix] != substring[i]:
            increment_counter()
            current_prefix = prefix_arr[current_prefix - 1]
        increment_counter()
        if substring[current_prefix] == substring[i]:
            current_prefix += 1
        prefix_arr[i] = current_prefix
    return prefix_arr


def Knuth_Morris_Pratt_algorithm(substring: str, main_text: str) -> int:
    reset_counter()
    substr_len = len(substring)
    main_text_len = len(main_text)
    if substr_len == 0 or main_text_len == 0:
        return -1
    prefix_arr = make_prefix(substring)
    substr_index = 0
    for index in range(main_text_len):
        flag = True
        for j in range(substr_index, substr_len):
            increment_counter()
            if substring[j] != main_text[index + j]:
                substr_index = prefix_arr[j - 1]
                flag = False
                break
        if flag:
            return index
    return -1


def run_algorithms(substring_file: str, text_file: str) -> None:
    # Substring and text
    substring = read_file(substring_file)
    text = read_file(text_file)
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

    # Knuth–Morris–Pratt algorithm
    print("\n-----Knuth–Morris–Pratt algorithm-----")
    pos = Knuth_Morris_Pratt_algorithm(substring, text)
    print(f"Position of substring: {pos}")
    if pos > 0:
        print(f"\nText started with substring: {text[pos:]}")


if __name__ == "__main__":
    substring_file = "test/substr.txt"
    text_file = "test/text.txt"
    run_algorithms(substring_file, text_file)
