#! /usr/bin/env python3
'''
Search MobyGames for a given game
'''

# imports
from json import loads as jloads
from urllib.parse import quote
from urllib.request import Request, urlopen
import argparse

# constants
BASE_URL = 'https://api.mobygames.com/v1/games'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
MIN_YEAR = 0
MAX_YEAR = 2100
PLATFORM_ID = {
    'GB':      10,
    'GBA':     12,
    'GBC':     11,
    'GC':      14,
    'N64':      9,
    'PSX':      6,
    'PS2':      7,
    'PS3':     81,
    'PSP':     46,
    'Switch': 203,
    'Wii':    132,
    'XBOX':    13,
    'XBOX360': 69,
}

# main program
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--api_key', required=True, type=str, help="MobyGames API Key")
    parser.add_argument('-t', '--title', required=False, type=str, default=None, help="Title")
    parser.add_argument('-p', '--platform', required=False, type=str, default=None, help="Platform (options: %s)" % ', '.join(sorted(PLATFORM_ID.keys())))
    parser.add_argument('-o', '--output', required=False, type=str, default='stdout', help="Output File (TSV)")
    args = parser.parse_args(); url = BASE_URL

    # parse API key
    if not args.api_key.startswith('moby_'):
        raise ValueError("Invalid API Key (must start with 'moby_'): %s" % args.api_key)
    url += ('?api_key=%s' % args.api_key)

    # parse title
    if args.title is not None:
        url += ('&title=%s' % quote(args.title, safe=''))

    # parse platform
    platform_ID = None
    if args.platform is not None:
        try:
            platform_ID = PLATFORM_ID[args.platform.strip().upper()]
            url += ('&platform=%d' % platform_ID)
        except:
            raise ValueError("Invalid platform: %s" % args.platform)

    # search MobyGames
    req = Request(url, data=None, headers={'User-Agent':USER_AGENT})
    data = jloads(urlopen(req).read())
    if args.output.strip().lower() == 'stdout':
        from sys import stdout as out_f
    else:
        out_f = open(args.output, 'w')
    out_f.write('Title\tRelease Date\tPlatform\tGenre\tDescription (HTML)\n')
    for game_data in data['games']:
        out_f.write(game_data['title'])
        if args.platform is None:
            out_f.write('\t%s\t%s' % sorted((curr['first_release_date'].strip(),curr['platform_name'].strip()) for curr in game_data['platforms'])[0])
        else:
            tmp = None
            for curr in game_data['platforms']:
                if curr['platform_id'] == platform_ID:
                    tmp = (curr['first_release_date'].strip(), curr['platform_name'].strip()); break
            if tmp is None:
                out_f.write('\t\t')
            else:
                out_f.write('\t%s\t%s' % tmp)
        out_f.write('\t%s' % ', '.join(sorted(curr['genre_name'] for curr in game_data['genres'])))
        out_f.write('\t')
        if 'description' in game_data and game_data['description'] is not None:
            out_f.write('\t%s' % game_data['description'].replace('\n','').strip())
        out_f.write('\n')
    out_f.close()
