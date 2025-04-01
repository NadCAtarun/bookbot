import sys
from stats import count_words

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(book):
    print("--------- Character Count -------")
    chars = {}
    for c in book.lower():
        if not c.isalpha():
            continue
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    for c, n in sorted(chars.items(), key=lambda item: item[1], reverse=True):
        print(f"{c}: {n}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book = read_book(book_path)
    count_words(book)
    count_characters(book)
    print("============= END ===============")

main()
