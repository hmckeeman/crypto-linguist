import praw
import configparser

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve the Reddit API credentials from the configuration file
client_id = config.get('reddit', 'client_id')
client_secret = config.get('reddit', 'client_secret')
user_agent = config.get('reddit', 'user_agent')
username = config.get('reddit', 'username')
password = config.get('reddit', 'password')

# Initialize the Reddit API instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
)

# Access the desired subreddit
subreddit = reddit.subreddit('cryptocurrency')

# Retrieve the top posts containing the word 'shill'
top_posts = subreddit.search('shill', sort='top', time_filter='all', limit=100)

# Save the raw post data to a file
with open('raw_data.txt', 'w') as file:
    for post in top_posts:
        file.write(post.selftext + '\n')
