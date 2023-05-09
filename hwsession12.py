

import nltk
nltk.download('punkt')

# Read the text files
with open('Political Economy.py', 'r', encoding='utf-8') as file:
    book1_text = file.read()

with open('Spenser's Faerie Queene.py', 'r', encoding='utf-8') as file:
    book2_text = file.read()

# Tokenize the text and create a set of unique words for each book
book1_words = set(nltk.word_tokenize(book1_text))
book2_words = set(nltk.word_tokenize(book2_text))

# Count the total number of words in each book
book1_total_words = len(nltk.word_tokenize(book1_text))
book2_total_words = len(nltk.word_tokenize(book2_text))

# Calculate the number of unique words in each book
book1_unique_words = len(book1_words)
book2_unique_words = len(book2_words)

# Calculate the ratio of unique words to total words for each book
book1_ratio = book1_unique_words / book1_total_words
book2_ratio = book2_unique_words / book2_total_words

# Print the results
print('Book 1 unique words:', book1_unique_words)
print('Book 2 unique words:', book2_unique_words)

if book1_unique_words > book2_unique_words:
    print('Book 1 has more unique words')
else:
    print('Book 2 has more unique words')

print('Book 1 unique to total ratio:', book1_ratio)
print('Book 2 unique to total ratio:', book2_ratio)

if book1_ratio > book2_ratio:
    print('Book 1 has a higher unique to total ratio')
else:
    print('Book 2 has a higher unique to total ratio')
