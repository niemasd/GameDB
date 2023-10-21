#! /usr/bin/env python3
'''
Build a titles.json file from game folders
'''
from glob import glob
from json import dump as jdump
data = dict()
for game_folder in sorted(glob('games/*')):
    serial = game_folder.rstrip('/').split('/')[-1].strip()
    data[serial] = ' / '.join([v.strip() for v in open('%s/title.txt' % game_folder).read().strip().splitlines()])
f = open('titles.json', 'w')
jdump(data, f)
f.close()
