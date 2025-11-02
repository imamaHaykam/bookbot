import sys
from stats import word_count
from stats import character_count
from stats import character_frequency

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    book_content = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_content)} total words")
    print("--------- Character Count -------")
    char_counts = character_frequency(book_content)
    for char_dict in char_counts:
        char = char_dict['char']
        count = char_dict['count']
        print(f"{char}: {count}")
    print("============ END ===============")

if __name__ == "__main__":
    main()    