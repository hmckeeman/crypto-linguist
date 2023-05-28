import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import string

# Load the clean data from the file
with open('clean_shill_data.txt', 'r', encoding='utf-8') as file:
    clean_data = file.read()

# Tokenize the clean data into individual words
tokenizer = nltk.RegexpTokenizer(r'\w+')
words = tokenizer.tokenize(clean_data.lower())

# Remove punctuation
words = [word for word in words if word not in string.punctuation]

# Create a bigram collocation finder
finder = BigramCollocationFinder.from_words(words)

# Calculate the collocation scores using Pointwise Mutual Information (PMI)
bigram_measures = BigramAssocMeasures()
collocations = finder.score_ngrams(bigram_measures.pmi)

# Sort the collocations by score in descending order
collocations = sorted(collocations, key=lambda x: -x[1])

# Extract the top ten collocates
top_collocates = collocations[:10]

# Write the top collocates to the output file
with open('shill_collocates.txt', 'w', encoding='utf-8') as file:
    for i, (collocate, score) in enumerate(top_collocates, start=1):
        file.write(f"{i}. {collocate[0]} {collocate[1]} (PMI: {score:.2f})\n")
