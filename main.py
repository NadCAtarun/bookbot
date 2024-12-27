
def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(book):
    print(f"{len(book.split())} words found in the document")

def count_characters(book):
    chars = {}
    for c in book.lower():
        if not c.isalpha():
            continue
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c, n in sorted(chars.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{c}' character was found {n} times")

def main():
    book_path = f"books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    book = read_book(book_path)
    count_words(book)
    print()
    count_characters(book)
    print("--- End report ---")

main()
