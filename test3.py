import tweepy

# Your Twitter API credentials
consumer_key = 'OAw1JDsrAkRKFdmSq7JwtNcFX'
consumer_secret = 'hl9dfhAsY3Xb0W8qCTym5tzpp6yea7W2hsUVHiwl4WaJ2UHgFd'
access_token = '1520349457572937729-NwzfPZKLztKfWuSGhgNI3BLV59axLt'
access_token_secret = '2QHtzKd0V6j9kFaYwOYRBqX7Ooo4Y8kmorZWsFvPk0cm6'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Fetch tweets by Elon Musk
tweets = api.user_timeline(screen_name='elonmusk', count=10, tweet_mode='extended')

# Print tweet texts and creation dates
for tweet in tweets:
    print(tweet.created_at, tweet.full_text)
