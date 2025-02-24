from stats import count_words, character_counter, dictionary_sorter
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    book_content = get_book_text(sys.argv[1])
    num_words = count_words(book_content)
    num_characters = character_counter(book_content)
    print('============ BOOKBOT ============')
    print("Analyzing book found at books/frankenstein.txt")
    print('----------- Word Count ----------')
    print(f"Found {num_words} total words")
    print('----------- Character Count ----------')
    dictionary_sorter([num_characters]) 

print(sys.argv, len(sys.argv))
main()