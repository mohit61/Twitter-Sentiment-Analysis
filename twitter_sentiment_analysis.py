#For accessing twitter api
import tweepy
#For performing sentimate analysis
from textblob import TextBlob

import csv

# Step 1 - Authenticate
consumer_key= 'xxxxxxxxx'
consumer_secret= 'xxxxxxxxxxx'

access_token='xxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 2 - Retrieve Tweets
public_tweets = api.search('salman khan')

#Step 3 - Performing sentiment analysis and labelling each sentiment as 'POSITIVE', 'NEGATIVE' and 'NEUTRAL'
with open('sentiment.csv', 'w') as file:
	for tweet in public_tweets:
			#TRY PRINTING THIS
	    #print(tweet.text)

	    file_writer = csv.writer(file)

	    #Step 4 Perform Sentiment Analysis on Tweets
	    analysis = TextBlob(tweet.text)

	    #TRY PRINTING THIS
	    #print(analysis.sentiment)

	    #Labelling as positive , negative and neutral on the basis of polarity
	    if analysis.sentiment.polarity>0:
	    	sentiment = "POSITIVE"
	    elif analysis.sentiment.polarity<0:
	    	sentiment = "NEGATIVE"
	    else:
	    	sentiment= "NEUTRAL"

	    #Writing to csv file in 2 columns as tweet text and sentiment
	    file_writer.writerow([tweet.text,sentiment])
	    

	#polarity measures how positive or negative some text is
	#and subjectivity measures how much opinion the text is vs how much factual the text is 

#NOTES:
	# sentiment analysis - understanding and extracting feelings from data

	# and api lets you access an apps functionality from your code
