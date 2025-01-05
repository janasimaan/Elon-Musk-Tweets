#import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#import yfinance as yf
import GetOldTweets3 as got

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
tweet_query = got.manager.TweetCriteria().setUsername("elonmusk").setSince("2011-01-01").setHeaders(headers)  # Set headers

#historical data of Elon Musk's tweets:-
# Read the CSV file into a DataFrame
tweets_df = pd.read_csv('TweetsElonMusk.csv')

# Define a query for Elon Musk's tweets
tweet_query = got.manager.TweetCriteria().setUsername("elonmusk").setSince("2011-01-01")  # Adjust start date as needed

# Fetch historical tweets based on the query
tweets = got.manager.TweetManager.getTweets(tweet_query)

# Create a list of dictionaries to store tweet data
tweet_data = []
for tweet in tweets:
    tweet_data.append({
        'date': tweet.date,
        'text': tweet.text
    })

# Create a DataFrame from the list of dictionaries
tweets_df = pd.DataFrame(tweet_data)

# Keywords related to Tesla and SpaceX
tesla_keywords = ['tesla', 'electric car', 'EV', 'electric vehicle']
spacex_keywords = ['spacex', 'rocket', 'space exploration', 'mars']

# Create masks for relevant tweets
tesla_mask = tweets_df['tweet'].str.contains('|'.join(tesla_keywords), case=False)
spacex_mask = tweets_df['tweet'].str.contains('|'.join(spacex_keywords), case=False)

# Filter tweets for Tesla and SpaceX
tesla_tweets = tweets_df[tesla_mask]
spacex_tweets = tweets_df[spacex_mask]

# Print filtered tweets
print("Tesla Tweets:")
print(tesla_tweets[['date', 'tweet']])  # Display date and tweet columns

print("\nSpaceX Tweets:")
print(spacex_tweets[['date', 'tweet']])  # Display date and tweet columns


"""
# Preprocess stock price data
tesla_history = tesla.history(period="2y")
spacex_history = spacex.history(period="2y")

# Merge tweet data with stock price data based on date index
tesla_spacex_tweets['date'] = pd.to_datetime(tesla_spacex_tweets['date'])
tesla_history.index = pd.to_datetime(tesla_history.index)

merged_data = tesla_spacex_tweets.merge(tesla_history, left_on='date', right_index=True, how='left')

# Save preprocessed data to a new CSV file
merged_data.to_csv('preprocessed_data.csv', index=False)
"""






