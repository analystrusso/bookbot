def main():
    book_path = "github.com/analystrusso/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print("Word count:", countwords(text))
    
def countwords(text):
    wordcount = len(text.split())
    return wordcount

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()