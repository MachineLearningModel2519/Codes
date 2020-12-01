import os
import tweepy as tw
import pandas as pd
consumer_key= 'hIOhjmcCX8oFw5QAKtVOP6y0d'
consumer_secret= 'UHk3DQs2JpZ61pXZ0V8xONPtKbD3VUdC23seyiR6FyVtZjuasL'
access_token= '1239282371750326272-2bP6ZQ0oMBOmOoBFMfqWxGRQXyYy6u'
access_token_secret= 'MUkb69wgsG5Wk3VJc4UhJCJmD2oCBx4J3Vs4dEnfMNpI7'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
search_words = "#covid"
date_since = "2020-03-20"
new_search = search_words + " -filter:retweets"
new_search
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(5)
                   
for tweet in tweets:    
     users_locs = [[tweet.user.screen_name, tweet.text] for tweet in tweets]

tweet_text = pd.DataFrame(data=users_locs, columns=['user', "tweet"])
tweet_text
