#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--hashtags',nargs='+',required=True)
args = parser.parse_args()

import matplotlib
matplotlib.use('Agg')
import os
import re
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

total = {}

for hashtag in args.hashtags:
    dayCount = {}
    for filename in sorted(os.listdir('outputs')):
        dayTweets = os.path.join('outputs', filename)
        date = filename[10:18]
        if os.path.isfile(dayTweets) and 'lang' in dayTweets:
            tweetCount = 0
            with open(dayTweets) as file:
                data = json.load(file)
                for k in data:
                    if hashtag == k:
                        for key in data[k]:
                            tweetCount += data[k][key]
            dayCount[date] = tweetCount
    total[hashtag] = dayCount

plt.figure(figsize=(14, 8))
for hashtag, dates_counts in total.items():
    dates_sorted = sorted(dates_counts.keys())
    counts = [dates_counts[date] for date in dates_sorted]
    plt.plot(dates_sorted, counts, label=hashtag)

plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Tweet Counts by Hashtag Over Time')
all_dates = list(sorted(total[next(iter(total))].keys()))
selected_dates = all_dates[::20]
plt.xticks(selected_dates, rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('hashtag_trends.png')
plt.close()
