#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import glob
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from datetime import datetime


# load each of the input paths
total = defaultdict(lambda: Counter())
for path in glob.glob('outputs/geoTwitter*.country'):
    with open(path) as f:
        tmp = json.load(f)
        filename = os.path.basename(path)
        date = filename[10:18]
        # iterate over args.keys, sum occurrences 
        for key in args.keys:
            if key in tmp:
                total[key][date] = []
                try:
                    total[key][date].append(sum(tmp[key].values()))
                except KeyError:
                    pass

# create graphs

fig, ax = plt.subplots()
for key in args.keys:
    dates = sorted(total[key].keys())
    values = [sum(total[key][date]) for date in dates]
    days = [datetime.strptime(date, '%y-%m-%d') for date in dates]
    ax.plot(days, values, label=key)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))

ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))

ax.set_xlabel('Date')
ax.set_ylabel('Number of Tweets')
ax.legend()

# save plot
tags = [key[1:] for key in args.keys]
plt.savefig('_'.join(tags)+'.png')
