def print_upper_words(words,letters):
    """Print out each word on separate line in uppercase"""
    for word in words:
        for letter in letters:
            if word.startswith(letter):
                print (word.upper())
