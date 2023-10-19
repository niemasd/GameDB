#! /usr/bin/env python3
'''
Plot a histogram of release dates from game folders
'''
from datetime import datetime
from glob import glob
from seaborn import histplot
import matplotlib.pyplot as plt

# load dates and regions
dates = list(); regions = list()
for txt in glob('games/*/release_date.txt'):
    data = open(txt).read().strip()
    try:
        release_date = datetime.strptime(data, '%Y-%m-%d')
    except:
        try:
            release_date = datetime.strptime(data, '%Y-%m')
        except:
            release_date = datetime.strptime(data, '%Y')
    dates.append(release_date)
    regions.append(open(txt.replace('release_date.txt','region.txt')).read().strip())

# plot dates
fig, ax = plt.subplots(figsize=(10,5))
histplot(x=dates, hue=regions, multiple="stack", legend=True)
plt.xlabel("Release Date")
plt.ylabel("Number of Games")
fig.savefig('release_dates.pdf', format='pdf', bbox_inches='tight')
