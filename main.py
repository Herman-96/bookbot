from stats import wordCounter, get_num_letters, sort_letters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = wordCounter(path)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    letter_count = get_num_letters(path)
    sorted_letters = sort_letters(letter_count)
    for letter_dict in sorted_letters:
        char = letter_dict["char"]
        count = letter_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main() 
