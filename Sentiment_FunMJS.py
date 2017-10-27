import tweepy

from textblob import TextBlob

consumer_key = "B8LNqblvf1nTDchn3nVWqXqGz"
consumer_secret = "C60m5RQ3SPgvbKtF3sdYFuCo5CHYF7cGK1UBRi0vdwHdFbTPu8"

access_token = "586110232-w1YQGI3IMjjQtwrTOMReuzz2yI8UFhI0Kbew92dF"
access_token_secret = "z8qURjJF9VADG3FGiTbDwfvmlvAutOuNJ3bL9g60g6hx0"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Shearing")
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


