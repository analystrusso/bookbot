def main():
    book_path = "/home/adamrusso/workspace/github.com/analystrusso/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = countwords(text)
    character_dict = charactercount(text)

    items = [{"char": char, "count": count} for char, count in character_dict.items()]

    items.sort(key=lambda x: x["count"], reverse=True)

    print(f"--- Begin book report of {book_path}---\n")
    print(f"Word count: {word_count}\n")
    
    for item in items:
        char = item["char"]
        if char.isalpha():
            print(f"The '{item['char']}' character was found {item['count']:>5} times")
    
    print(f"\n--- End report ---")
    
def countwords(text):
    return len(text.split())


def charactercount(text):
    characterdict = {}

    for char in text:
        char = char.lower()

        characterdict[char] = characterdict.get(char, 0) + 1

    return characterdict

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()