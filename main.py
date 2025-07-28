# This is a program to print out a book

from stats import book_path, get_book_text, get_word_count, get_char_count, sorting_char_dict, report
import sys

def main():

    bookpath = book_path(sys.argv)
    text = get_book_text(bookpath)
    number_words = get_word_count(text)
    char_dict = get_char_count(text)
    sorted_list = sorting_char_dict(char_dict)
    report(bookpath, number_words, sorted_list)


main()
