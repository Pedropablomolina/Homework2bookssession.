import nltk
from nltk.corpus import stopwords

# Load and preprocess the text files
book1 = open('book1.txt', 'r').read()
book2 = open('book2.txt', 'r').read()

stop_words = set(stopwords.words('english'))

# Remove unwanted characters and stopwords
book1_tokens = nltk.word_tokenize(book1.lower())
book1_tokens = [word for word in book1_tokens if word.isalpha() and word not in stop_words]

book2_tokens = nltk.word_tokenize(book2.lower())
book2_tokens = [word for word in book2_tokens if word.isalpha() and word not in stop_words]

# Calculate unique word count
book1_unique_words = set(book1_tokens)
book2_unique_words = set(book2_tokens)

num_unique_words_book1 = len(book1_unique_words)
num_unique_words_book2 = len(book2_unique_words)

# Calculate total word count
num_words_book1 = len(book1_tokens)
num_words_book2 = len(book2_tokens)

# Calculate unique to total word ratio
unique_to_total_ratio_book1 = num_unique_words_book1 / num_words_book1
unique_to_total_ratio_book2 = num_unique_words_book2 / num_words_book2

# Compare the results
if num_unique_words_book1 > num_unique_words_book2:
    print("Book 1 has more unique words")
else:
    print("Book 2 has more unique words")

if unique_to_total_ratio_book1 > unique_to_total_ratio_book2:
    print("Book 1 has a higher ratio of unique to total words")
else:
    print("Book 2 has a higher ratio of unique to total words")

