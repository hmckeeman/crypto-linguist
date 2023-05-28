import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter

# Load the clean data from the file
with open('clean_shill_data.txt', 'r') as file:
    clean_data = file.read()

# Tokenize the clean data into words
words = word_tokenize(clean_data)

# Tag the part of speech for each word using NLTK's pos_tag
pos_tags = pos_tag(words)

# Find instances of "shill" and their corresponding part of speech tags
shill_pos_tags = [tag[1] for tag in pos_tags if tag[0].lower() == 'shill']

# Calculate the percentage of each part of speech tag for "shill"
pos_counts = Counter(shill_pos_tags)
total_shill_instances = len(shill_pos_tags)
pos_percentages = {pos: count / total_shill_instances * 100 for pos, count in pos_counts.items()}

# Save the results to a file
with open('shill_POS_percents.txt', 'w') as file:
    for pos, percentage in pos_percentages.items():
        file.write(f"{pos}: {percentage:.2f}%\n")
