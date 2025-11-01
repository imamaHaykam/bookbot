from stats import word_count
from stats import character_count
from stats import character_frequency

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def main():
    book_content = get_book_text('books/frankenstein.txt')
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_content)} total words")
    print("--------- Character Count -------")
    char_counts = character_frequency(book_content)
    for char_dict in char_counts:
        char = char_dict['char']
        count = char_dict['count']
        print(f"{char}: {count}")
    print("============ END ===============")
main()