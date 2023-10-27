#! /usr/bin/env python3
'''
Rename regions to be NTSC-U, NTSC-PAL, or NTSC-J
'''
from glob import glob

# region map
REGION = {
    'Asia':                 'NTSC-J',
    'Australia':            'PAL',
    'AUSTRALIAN':           'PAL',
    'Austria':              'PAL',
    'Austria, Switzerland': 'PAL',
    'Belgium':              'PAL',
    'Belgium, Netherlands': 'PAL',
    'Brazil':               'NTSC-U',
    'China':                'NTSC-J',
    'CHINESE':              'NTSC-J',
    'Croatia':              'PAL',
    'Denmark':              'PAL',
    'Europe':               'PAL',
    'Europe, Australia':    'PAL',
    'Finland':              'PAL',
    'France':               'PAL',
    'France, Spain':        'PAL',
    'Germany':              'PAL',
    'Greece':               'PAL',
    'India':                'PAL',
    'Ireland':              'PAL',
    'Italy':                'PAL',
    'Japan':                'NTSC-J',
    'Japan, Asia':          'NTSC-J',
    'Japan, Korea':         'NTSC-J',
    'Korea':                'NTSC-J',
    'KOREAN':               'NTSC-J',
    'Latin America':        'PAL',
    'Netherlands':          'PAL',
    'Norway':               'PAL',
    'NTSC-J':               'NTSC-J',
    'NTSC-U':               'NTSC-U',
    'PAL':                  'PAL',
    'Poland':               'PAL',
    'Portugal':             'PAL',
    'Russia':               'PAL',
    'Scandinavia':          'PAL',
    'South Africa':         'PAL',
    'Spain':                'PAL',
    'Spain, Portugal':      'PAL',
    'Sweden':               'PAL',
    'Switzerland':          'PAL',
    'Taiwan':               'NTSC-J',
    'UK':                   'PAL',
    'UK, Australia':        'PAL',
    'USA':                  'NTSC-U',
    'USA, Brazil':          'NTSC-U',
    'USA, Canada':          'NTSC-U',
    'World':                'NTSC-U',
}

# main program
if __name__ == "__main__":
    for fn in glob('*/region.txt'):
        r = open(fn).read().strip()
        if r not in REGION:
            print("Missing Region: %s" % r); exit(1)
        f = open(fn, 'w'); f.write('%s\n' % REGION[r]); f.close()
