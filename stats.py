def get_word_count(contents):
    words=contents.split()
    count=len(words)
    count_msg= (f"{count} words found in the document")
    return count_msg