import tweepy

consumer_key =  "key"
consumer_secret = "secret"
access_token = "token"
access_token_secret = "token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweet = "Some text"

api = tweepy.API(auth)
api.update_status(tweet)
