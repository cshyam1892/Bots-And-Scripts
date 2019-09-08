#!/usr/bin/env python3

import datetime as dt
import praw
import pandas as pd

reddit = praw.Reddit(client_id='xxxxxxxxxxxxxx',
                     client_secret='xxxxxxxxxxxxxxxxxxxxxxxxxxx',
                     user_agent='checkpost',
                     username='xxxxxxx',
                     password='xxxxxxxxxxxx')
subreddit = reddit.subreddit('programming')
top_subreddit = subreddit.hot(limit=5)

#parsing and downloading the data
#for submission in subreddit.hot(limit=10):
#    print(submission.title, submission.id)

topics_dict = {"title": [],
               "score": [],
               "id": [],
               "comms_num": [],
               "created": [],
               "body": [],
              }

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

#spreedsheet in panda
topics_data = pd.DataFrame(topics_dict)

def get_data(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_data)

#exporting a csv
topics_data.to_csv('check.csv', index=False)



