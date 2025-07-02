import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(file_path):
    """
        function for getting the contents of a file and return it as a string
    """
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = count_words(file_contents)
    character_freq = count_characters(file_contents)
    sorted_characters = sort_characters(character_freq)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

    
    

main()