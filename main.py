from collections import defaultdict

def count_words(text: str):
    return len(text.split())

def read_book(title: str):
    with open(f"books/{title}.txt") as f:
       return f.read()

def count_characters(text: str):
    char_map = defaultdict(int)
    for c in text:
        char_map[c.lower()] +=1
    return char_map

def print_report(title: str):
    book_content = read_book(title)
    print(f"--- Begin report of books/{title}.txt ---")
    print(f"{count_words(book_content)} words found in the document")
    print("") 
    for k, v in count_characters(book_content).items():
        if k.isalpha():
            print(f"The {k} character was found {v} times")
    print("--- End report --") 

def main():
    book_title = "Frankenstein"
    print_report(book_title)

if __name__ == '__main__':
    main()