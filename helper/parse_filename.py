#! /usr/bin/env python3
'''
Parse a filename to extract the title, region, language(s), etc. and print as TSV
'''

# imports
from sys import argv

# languages
LANGUAGES = {
    'Ar':    'Arabic',
    'Ca':    'Catalan',
    'Cs':    'Czech',
    'Da':    'Danish',
    'De':    'German',
    'En':    'English',
    'En-GB': 'English',
    'En-US': 'English',
    'Es':    'Spanish',
    'Fi':    'Finnish',
    'Fr':    'French',
    'It':    'Italian',
    'Ja':    'Japanese',
    'Ko':    'Korean',
    'Nl':    'Dutch',
    'No':    'Norwegian',
    'Pl':    'Polish',
    'Pt':    'Portuguese',
    'Ro':    'Romanian',
    'Ru':    'Russian',
    'Sv':    'Swedish',
    'Zh':    'Simplified Chinese',
}
LANGUAGES |= {'%s+%s' % (k1,k2) : '%s / %s' % (v1,v2) for k1,v1 in LANGUAGES.items() for k2,v2 in LANGUAGES.items()}

# regions
REGIONS = {
    'Australia',
    'Austria',
    'Belgium',
    'Brazil',
    'Canada',
    'China',
    'Denmark',
    'Europe',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Ireland',
    'Israel',
    'Italy',
    'Japan',
    'Korea',
    'Netherlands',
    'Norway',
    'Poland',
    'Portugal',
    'Russia',
    'Scandinavia',
    'Spain',
    'Sweden',
    'Taiwan',
    'UK',
    'United Kingdom',
    'USA',
    'World',
}

# main program
if __name__ == "__main__":
    assert len(argv) == 2, "USAGE: %s <filename>" % argv[0]
    fn = argv[1].strip(); meta = dict()
    if fn.endswith('.gz'):
        fn = fn[:-3]
    fn = '.'.join(fn.split('.')[:-1]); fn_parts = fn.replace(')','').split(' ('); i = 1
    while i < len(fn_parts):
        meta_parts = [v.strip() for v in fn_parts[i].split(',')]
        if meta_parts[0] in REGIONS:
            meta['region'] = ' / '.join(meta_parts)
        elif meta_parts[0] in LANGUAGES:
            meta['language'] = ' / '.join(LANGUAGES[v] for v in meta_parts)
        if meta_parts[0] in REGIONS or meta_parts[0] in LANGUAGES:
            del fn_parts[i]
        else:
            i += 1
    if len(fn_parts) == 1:
        meta['title'] = fn_parts[0].strip()
    else:
        meta['title'] = '%s (%s)' % (fn_parts[0].strip(), ') ('.join(fn_parts[1:]))
    for tup in meta.items():
        print('%s\t%s' % tup)
