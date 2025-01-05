import pandas as pd
import yfinance as yf
from textblob import TextBlob
import pytz
import numpy as np

#step 1 - Data Collection:
# Load tweet and stock price data
tweets_df = pd.read_csv('TweetsElonMusk.csv')
tesla = yf.Ticker("TSLA")
spacex = yf.Ticker("SPCE")

# Preprocess tweet data
tesla_keywords = ['tesla', 'electric car', 'EV', 'electric vehicle']
spacex_keywords = ['spacex', 'rocket', 'space exploration', 'mars']

# Filter tweets based on keywords
tesla_mask = tweets_df['tweet'].str.contains('|'.join(tesla_keywords), case=False)
spacex_mask = tweets_df['tweet'].str.contains('|'.join(spacex_keywords), case=False)

# Create a copy of tweets that match the keywords
tesla_spacex_tweets = tweets_df[tesla_mask | spacex_mask].copy()

# Perform sentiment analysis on tweets
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

# Use .loc to set the sentiment value
tesla_spacex_tweets.loc[:, 'sentiment'] = tesla_spacex_tweets['tweet'].apply(analyze_sentiment)

# Preprocess stock price data
tesla_history = tesla.history(period="2y")
spacex_history = spacex.history(period="2y")


#step 2 - Data Preprocessing:
# Convert time zones to match before merging
tesla_spacex_tweets['date'] = pd.to_datetime(tesla_spacex_tweets['date'])
tesla_spacex_tweets['date'] = tesla_spacex_tweets['date'].dt.tz_localize('UTC')

# Merge tweet data with stock price data based on date index
merged_data = tesla_spacex_tweets.merge(tesla_history, left_on='date', right_index=True, how='left')

# Save preprocessed data to a new CSV file
merged_data.to_csv('preprocessed_data.csv', index=False)

#step 3 - Sentiment Analysis:
# Categorize sentiment based on sentiment score
def categorize_sentiment(score):
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment categorization to the DataFrame
merged_data['sentiment_category'] = merged_data['sentiment'].apply(categorize_sentiment)

# Print the DataFrame with sentiment categories
print(merged_data[['date', 'tweet', 'sentiment_category']])

#step 4 - Correlation Analysis:-
# Calculate the Pearson correlation between sentiment and stock price
correlation_tesla = merged_data['sentiment'].corr(merged_data['Close'])  # Replace 'Close' with the appropriate column name for stock price
correlation_spacex = merged_data['sentiment'].corr(merged_data['Close'])  # Replace 'Close' with the appropriate column name for stock price

print(f"Pearson Correlation (Tesla): {correlation_tesla:.2f}")
print(f"Pearson Correlation (SpaceX): {correlation_spacex:.2f}")
