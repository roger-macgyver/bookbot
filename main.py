def get_book_text(path_to_file):
    with open (path_to_file) as f:
        contents=f.read()
    return contents
def get_word_count(contents):
    words=contents.split()
    count=len(words)
    count_msg= (f"{count} words found in the document")
    return count_msg



def main():
    contents = get_book_text("books/frankenstein.txt")
    count_msg = get_word_count(contents)
    print (count_msg)  
main()