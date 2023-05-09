# Load the text files
with open('book1.txt', 'r') as f:
    book1 = f.read()
with open('book2.txt', 'r') as f:
    book2 = f.read()

# Define a function to preprocess the text
def preprocess(text):
    # Remove unwanted characters and punctuation
    text = text.lower()
    for char in '.,:;?!()[]{}-–"—\'\"':
        text = text.replace(char, ' ')
    # Split the text into words
    words = text.split()
    # Remove stopwords
    stopwords = set(['the', 'and', 'of', 'to', 'in', 'a', 'that', 'it', 'with', 'is', 'was', 'for', 'as', 'on', 'by', 'at', 'an', 'be', 'this', 'which', 'not', 'are', 'from'])
    words = [word for word in words if word not in stopwords]
    return words

# Preprocess the text
book1_words = preprocess(book1)
book2_words = preprocess(book2)

# Calculate unique word count
book1_unique_words = set(book1_words)
book2_unique_words = set(book2_words)

num_unique_words_book1 = len(book1_unique_words)
num_unique_words_book2 = len(book2_unique_words)

# Calculate total word count
num_words_book1 = len(book1_words)
num_words_book2 = len(book2_words)

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
