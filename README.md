# Elon-Musk-Tweets
Step 1 - Data collection:
Loading the file of Elon's tweets that we downloaded from Kaggle, and the information about the stocks from the yfinance library.

Step 2 - Data preprocessing:
At this stage, we take from all the tweets only the tweets related to Tesla and Space X according to an array of strings that we defined, which contains strings that are keywords that we can use to find the tweets that are only related to Tesla and Space X.
And finally, we copy them so that we can access them "because there are instructions from Twitter for using tweets that are taken from any account".

Step 3 - Sentiment Analysis:
First we perform sentiment classification using the categorize_sentiment(score) function, this function categorizes a sentiment based on the sentiment score provided as input, and this is done using a textblob.
* When a sentence is passed to a Textblob it gives two outputs, which are polarity and subjectivity. Polarity is the output that is between [-1,1], where -1 refers to negative sentiment and +1 refers to positive sentiment.*
Now according to the function we built:
-) If the sentiment score is greater than 0, the tweet is considered positive.
-) If the sentiment score is less than 0, the tweet is considered negative.
-) If the sentiment score is 0, the tweet is considered neutral.
categorize_sentiment is added to your DataFrame to store the sentiment category. The cat categorize_sentiment function takes the sentiment score as input and returns the category The corresponding sentiment.
The .apply function is used to apply this classification function to the entire sentiment column.
