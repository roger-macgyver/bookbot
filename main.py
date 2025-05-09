from stats import get_word_count
from stats import get_character_count
#from stats import sort_data
def get_book_text(path_to_file):
    with open (path_to_file) as f:
        contents=f.read()
    return contents
def main():
    contents = get_book_text("books/frankenstein.txt")
    count_msg = get_word_count(contents)
    count = get_character_count(contents)
    print (count_msg, count) 
     
main()