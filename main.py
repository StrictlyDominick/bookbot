def main():
    book_path = "books/frankenstein.txt"
    print_book_report(book_path)

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

def print_book_report(book_path):
    print(f"--- Begin report of {book_path} ---")
    book_contents = get_book_contents(book_path)

    print(f"{count_words(book_contents)} words found in the document")
    print("")
    
    dict_of_char_counts = count_all_chars(book_contents)
    dict_list_keys = list(dict_of_char_counts.keys())
    dict_list_keys.sort()
    
    for key in dict_list_keys:
        if key.isalpha():
            print(f"The '{key}' character was found {dict_of_char_counts[key]} times.")

    print("--- End report ---")

main()