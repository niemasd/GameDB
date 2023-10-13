#! /usr/bin/env python3
'''
Build a complete data.json file from game folders
'''
from glob import glob
from json import dump as jdump
data = dict()
for game_folder in sorted(glob('games/*')):
    serial = game_folder.rstrip('/').split('/')[-1].strip()
    curr = dict()
    for txt in sorted(glob('%s/*.txt' % game_folder)):
        meta = txt.split('/')[-1].split('.txt')[0].strip()
        contents = [v.strip() for v in open(txt).read().strip().splitlines()]
        if len(contents) == 1:
            curr[meta] = contents[0]
        elif len(contents) > 1:
            curr[meta] = contents
    data[serial] = curr
f = open('data.json', 'w')
jdump(data, f)
f.close()
