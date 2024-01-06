def get_book_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(txt):
    return len(txt.split())

def main():
    book_content = get_book_contents("books/frankenstein.txt")
    words_counted = count_words(book_content)

    return print(words_counted)

main()