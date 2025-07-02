def count_words(contents):
    """
        function that accepts the text from the book as a string, 
        and returns the number of words in the string.
    """ 
    word_count = 0
    word_list = contents.split()

    for word in word_list:
        word_count += 1

    return word_count

def count_characters(contents):
    """
        takes the text from the book as a string, 
        and returns the number of times each character, 
        (including symbols and spaces), appears in the string
    """
    character_freq = {}
    contents = contents.lower()
    for character in contents:
        if character in character_freq:
            character_freq[character] += 1
        else:
            character_freq[character] = 1
    
    return character_freq

def sort_on(items):
    return items["num"]

def sort_characters(character_dict):
    """
        takes the dictionary of characters and their counts and 
        returns a sorted list of dictionaries.
    """
    character_list = [{"char": i, "num": j} for i, j in character_dict.items()]
    character_list.sort(reverse=True, key=sort_on)
    
    return character_list
    


    
