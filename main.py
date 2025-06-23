from stats import get_num_words
from stats import count_characters
from stats import sort_dict
import sys 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    file_path = "".join(sys.argv[1:])
    text = get_book_text(file_path)
    num_of_words = get_num_words(text)
    counter = count_characters(text)
    sorted_counter = sort_dict(counter)
    print(7*"-", "Word Count", 7*"-", end="\n")
    print(f"Found {num_of_words} total words")
    for item in sorted_counter:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

main()