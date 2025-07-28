 # stat functions
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def get_word_count(text):
    word_count = text.split()
    return len(word_count)


def get_char_count(text):
    character_count = {}
    for char in text:
        if char.lower() in character_count:
            character_count[char.lower()] += 1
        else:
            character_count[char.lower()] = 1
    return character_count
    
def sort_on(d):
    return d["num"]

def sorting_char_dict(char_dict):
    sorted_dict = []
    for ch in char_dict:
        sorted_dict.append({"char":ch, "num":char_dict[ch]})
    sorted_dict.sort(reverse = True, key = sort_on)
    return sorted_dict

def report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    

    print("============= END ===============")


def book_path(file):
    if len(file) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        return file[1]
