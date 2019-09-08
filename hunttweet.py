#!/usr/bin/env python3

import twitter

api = twitter.Api(consumer_key='xxxxxxxxxxxxxxxx',
                  consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                  access_token_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                  access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

results = api.GetUserTimeline(screen_name="manutd", count=5)
tweets = [i.AsDict() for i in results]
for tweet in tweets:
    print(tweet['id'], tweet['text'])
