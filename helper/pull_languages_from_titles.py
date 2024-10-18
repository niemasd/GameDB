#! /usr/bin/env python3
'''
Parse a title.txt file and, if it contains languages, remove them from the title and create a language.txt file instead
'''

# imports
from glob import glob

# constants
LANGUAGES = {
    'Ar':      'Arabic',
    'Ca':      'Catalan',
    'Cs':      'Czech',
    'Da':      'Danish',
    'De':      'German',
    'En':      'English',
    'En-GB':   'English',
    'En-US':   'English',
    'Es':      'Spanish',
    'Fi':      'Finnish',
    'Fr':      'French',
    'It':      'Italian',
    'Ja':      'Japanese',
    'Ko':      'Korean',
    'Nl':      'Dutch',
    'No':      'Norwegian',
    'Pl':      'Polish',
    'Pt':      'Portuguese',
    'Ro':      'Romanian',
    'Ru':      'Russian',
    'Sv':      'Swedish',
    'Zh':      'Chinese',
    'Zh-Hans': 'Chinese',
    'Zh-Hant': 'Chinese',
}

# main program
if __name__ == "__main__":
    for fn in glob('games/*/title.txt'):
        title = open(fn).read().strip()
        if '(En,' in title:
            lang_start = title.index(' (En,')
            for lang_end in range(lang_start+1, len(title)):
                if title[lang_end] == ')':
                    break
            new_title = title[:lang_start] + title[lang_end+1:]
            langs = [LANGUAGES[s].strip() for s in title[lang_start+2:lang_end].split(',')]
            f = open(fn.replace('/title.txt','/language.txt'),'w')
            f.write('%s\n' % '\n'.join(langs)); f.close()
            f = open(fn,'w'); f.write('%s\n' % new_title.strip()); f.close()
