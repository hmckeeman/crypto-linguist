import re
from bs4 import BeautifulSoup

def clean_up_post_content(content):
    # Clean up the post content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Remove all links from the content
    for link in soup.find_all('a'):
        link.decompose()

    # Get the cleaned content
    cleaned_content = soup.get_text()

    # Remove URLs from the cleaned content
    cleaned_content = re.sub(r'http[s]?://\S+|www\.\S+', '', cleaned_content)

    # Split the cleaned content into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', cleaned_content)

    # Return the cleaned up sentences
    return sentences

# Open the file containing the raw post data
with open('raw_data.txt', 'r') as file:
    post_content = file.readlines()

# Open a text file for writing the cleaned up results
with open('clean_shill_data.txt', 'w') as file:
    post_number = 1

    # Iterate over the post content and extract sentences with 'shill'
    for content in post_content:
        # Clean up the post content using the clean_up_post_content function
        sentences = clean_up_post_content(content)

        # Check if the post contains any sentences with 'shill'
        shill_sentences = [sentence.strip() for sentence in sentences if 'shill' in sentence.lower()]

        # Write the post number and shill sentences to the file
        if shill_sentences:
            file.write(f"{post_number}.)\n")
            file.write('\n'.join(shill_sentences) + '\n\n')

            post_number += 1
