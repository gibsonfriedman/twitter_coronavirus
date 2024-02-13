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

date_pattern = re.compile(r'geoTwitter(\d{2}-\d{2}-\d{2})\.zip\.lang')
hashtag_counts = defaultdict(lambda: defaultdict(int))

for filename in sorted(os.listdir('outputs')):
    match = date_pattern.search(filename)
    if match:
        date = '20' + match.group(1)
        file_path = os.path.join('outputs', filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            for hashtag in args.hashtags:
                hashtag_count = 0
                if hashtag in data:
                    hashtag_count = sum(data[hashtag].values())
                hashtag_counts[hashtag][date] += hashtag_count

plt.figure(figsize=(12, 8))
for hashtag, dates in hashtag_counts.items():
    dates_sorted = sorted(dates.keys())
    counts = [dates[date] for date in dates_sorted]
    plt.plot(dates_sorted, counts, label=hashtag, marker='o')

plt.xlabel('Date')
plt.ylabel('Tweet Count')
plt.title('Tweet Counts by Hashtag Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('trends.png')
plt.close()

