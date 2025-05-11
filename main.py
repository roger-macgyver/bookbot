import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_data

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents

def main():
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command-line arguments
    path = sys.argv[1]
    
    contents = get_book_text(path)
    count_msg = get_word_count(contents)
    count = get_character_count(contents)
    sort = sort_data(count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(count_msg)
    for item in sort:
        print(f"{item['char']}: {item['count']}")

main()