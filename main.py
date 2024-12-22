def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    
    word_count = get_word_count(text)
    #print(f"{word_count} words found in the text")
    
    char_count = character_count(text)
    print(char_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

      
def get_word_count(text):
  words = text.split()
  return len(words)

def character_count(text):
  char_dict = {}
  for char in text:
    lower_char = char.lower()
    if lower_char in char_dict:
      char_dict[lower_char] += 1
    else:
      char_dict[lower_char] = 1
  return char_dict


main()
