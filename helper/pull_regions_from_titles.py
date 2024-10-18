#! /usr/bin/env python3
'''
Parse a title.txt file and, if it contains a region, remove it from the title and create a region.txt file instead
'''

# imports
from glob import glob

# constants
REGIONS = {
    'France':       'PAL',
    'Japan':        'NTSC-J',
    'Japan, Korea': 'NTSC-J',
    'Europe':       'PAL',
    'USA':          'NTSC-U',
    'USA, Brazil':  'NTSC-U',
}

# main program
if __name__ == "__main__":
    for fn in glob('games/*/title.txt'):
        title = open(fn).read().strip()
        for k,v in REGIONS.items():
            r = ' (%s)' % k
            if r in title:
                f = open(fn.replace('/title.txt','/region.txt'),'w')
                f.write('%s\n' % v); f.close()
                new_title = title.replace(r,'')
                f = open(fn,'w'); f.write('%s\n' % new_title.strip()); f.close()
