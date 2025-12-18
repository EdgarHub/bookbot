from stats import get_num_words, get_num_chars,sorted_dictionary
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    num_words = 0
    num_words = get_num_words(get_book_text())
    
    letters=get_num_chars(get_book_text())
    res = sorted_dictionary(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in res:
        for key, val in d.items():
            print(f"{key}: {val}")
    print("============= END ===============")
    
def get_book_text():
    with open(sys.argv[1]) as f:
    # f is a file object
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    main()
