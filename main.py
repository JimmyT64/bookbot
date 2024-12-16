def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = len(file_contents.split())
        lowercontents = file_contents.lower()
        print(f"There are {wordcount} words in this book")
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        char_count = {}
        for letter in alphabet:
            char_count[letter] = lowercontents.count(letter)
        sortchar = sorted(char_count,key=char_count.get)
        for c in sortchar:
            print(f"Letter {c} appears {char_count[c]} times")
    print("--End Report--")
main()