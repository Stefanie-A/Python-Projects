import tweepy

# Twitter API credentials
API_KEY = ' '
API_SECRET_KEY = ' '
ACCESS_TOKEN = ' '
ACCESS_TOKEN_SECRET = ' '

# Authenticate with Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create the API object
api = tweepy.API(auth)

# Fetch tweets from a user's timeline
username = input("Twitter username: ")
tweets = api.user_timeline(screen_name=username, count=10)

# Print the text of each tweet
for tweet in tweets:
    print(tweet.text)

