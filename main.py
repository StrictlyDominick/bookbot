def main():
    book = get_book_contents("books/frankenstein.txt")
    print(count_all_chars(book))

def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(txt):
    return len(txt.split())

def get_unique_chars(txt):
    char_list = []
    for i in range(0, len(txt)):
        if char_list.count(txt[i]) == 0:
            char_list.append(txt[i])
    return char_list

def count_all_chars(txt):
    char_counts = {}
    lowercase_txt = txt.lower()
    char_list = get_unique_chars(lowercase_txt)

    for char in char_list:
        char_counts[char] = lowercase_txt.count(char)

    return char_counts

main()