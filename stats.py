def get_word_count(contents):
    words=contents.split()
    count=len(words)
    count_msg= (f"{count} words found in the document")
    return count_msg
def get_character_count(contents):
    counts={}
    text=contents.lower()
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts 