import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 
	''' 
	Generic Twitter Class for sentiment analysis. 
	'''
	def __init__(self): 
		''' 
		Class constructor or initialization method. 
		'''
		# keys and tokens from the Twitter Dev Console 
		consumer_key = 'MpUpt88UFN1Z3zqIQgxKBbv7L'
		consumer_secret = 't2CljXKSOq2tyou4AIoOAuu4ZaB55K0Oavdw5ZO4TVqBUfP5oJ'
		access_token = '611455362-E1N5nznk6gYoHlHzzFxK8UChNUzZ9hVFt9EGRjpq'
		access_token_secret = 'gJTzutIIllho9XZ86hSI1mzZAeQntN92xsFl7EqAzTslT'

		# attempt authentication 
		try: 
			# create OAuthHandler object 
			self.auth = OAuthHandler(consumer_key, consumer_secret) 
			# set access token and secret 
			self.auth.set_access_token(access_token, access_token_secret) 
			# create tweepy API object to fetch tweets 
			self.api = tweepy.API(self.auth) 
		except: 
			print("Error: Authentication Failed") 

	def clean_tweet(self, tweet): 
		''' 
		Utility function to clean tweet text by removing links, special characters 
		using simple regex statements. 
		'''
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 

	def get_tweet_sentiment(self, tweet): #self is for an instance of TwitterClass 
		''' 
		Utility function to classify sentiment of passed tweet 
		using textblob's sentiment method 
		'''
		# create TextBlob object of passed tweet text 
		analysis = TextBlob(self.clean_tweet(tweet)) 
		# set sentiment 
        

		if analysis.sentiment.polarity > 0: 
			return 'positive'
		elif analysis.sentiment.polarity == 0: 
			return 'neutral'
		else: 
			return 'negative'

	def get_tweets(self, query, count = 10): 
		''' 
		Main function to fetch tweets and parse them. 
		'''
		# empty list to store parsed tweets 
		tweets = [] 

		try: 
			# call twitter api to fetch tweets 
			fetched_tweets = self.api.search(q = query, count = count) 

			# parsing tweets one by one 
			for tweet in fetched_tweets: 
				# empty dictionary to store required params of a tweet 
				parsed_tweet = {} 

				# saving text of tweet 
				parsed_tweet['text'] = tweet.text #creating a new key of 'text' with value = tweet.text
				# saving sentiment of tweet 
				parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

				# appending parsed tweet to tweets list 
				if tweet.retweet_count > 0: 
					# if tweet has retweets, ensure that it is appended only once 
					if parsed_tweet not in tweets: 
						tweets.append(parsed_tweet) 
				else: 
					tweets.append(parsed_tweet) 

			# return parsed tweets 
			return tweets 

		except tweepy.TweepError as e: 
			# print error (if any) 
			print("Error : " + str(e)) 
		
	def comparesentiment(self,tweets):
		pos= ['happy','good','love','excite','great','fun']

		neg = ['bad','mad','sad','depressing','stressful','hate']

 
		count = 0
		sentiment = ''
		print("TWEETS: ")
		shortened_tweets = tweets[:10]
		
		new_arr = []

		for tweet in shortened_tweets:
			new_arr.append(shortened_tweets)
		print(tweets)
		for tweet in tweets:
			if tweet in pos:  
				count = count + 1 
	
			elif tweet in neg:
				count = count - 1 
	

		if count == 0:
			sentiment = 'neutral'
		elif count > 0: 
			sentiment = 'positive'
		else:
			sentiment = 'negative'
		
		return(f"Sentiment mostly: {sentiment} Count: {count}")



def main(): 
	# creating object of TwitterClient Class 
	api = TwitterClient() 

	#user-inputted query
	print('****************************************************')
	query = input('Enter a word you would like to search tweets for: ')
	# calling function to get tweets 
	tweets = api.get_tweets(query, count = 200) #returned 
    

	# picking positive tweets from tweets 
	ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
	
	# picking negative tweets from tweets 
	ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
	
	# printing first 5 positive tweets 
	print("\n\nPositive tweets:") 
	for tweet in ptweets[:10]: 
		print(tweet['text']) 

	# printing first 5 negative tweets 
	print("\n\nNegative tweets:") 
	for tweet in ntweets[:10]: 
		print(tweet['text']) 

	print(api.comparesentiment(tweets))
	# percentage of positive tweets 
	print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
	# percentage of negative tweets 
	print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
	# percentage of neutral tweets 
	print("Neutral tweets percentage: {} %".format(100-((100*len(ptweets)/len(tweets)) + (100*len(ntweets)/len(tweets)))))


if __name__ == "__main__": 
	# calling main function 
	main() 


