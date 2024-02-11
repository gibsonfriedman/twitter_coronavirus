#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output_filename', required=True, help='Filename for the output PNG file')
args = parser.parse_args()


# imports
import matplotlib
matplotlib.use('Agg')
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

def create_bar_graph(data, file_name):
    sorted_data_desc = sorted(data.items(), key=lambda item: item[1], reverse=True)[:10]
    sorted_data_asc = sorted(sorted_data_desc, key=lambda item: item[1])
    keys = [k for k, v in sorted_data_asc]
    values = [v for k, v in sorted_data_asc]

    plt.figure(figsize=(10, 8))
    plt.bar(range(len(keys)), values, color='blue', tick_label=keys)
    plt.xlabel('Keys')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)

    plt.savefig(f'{args.output_filename}.png', bbox_inches='tight')
    plt.close()

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

key_data = counts.get(args.key, {})
create_bar_graph(key_data, os.path.basename(args.input_path).split('.')[0])

