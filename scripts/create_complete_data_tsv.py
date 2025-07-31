#! /usr/bin/env python3
'''
Build a complete data.tsv file from game folders
'''
from glob import glob
from os.path import isfile
all_meta = ['title'] + sorted({txt.split('/')[-1].split('.txt')[0].strip() for txt in glob('games/*/*.txt')} - {'title'}) # put title first
f = open('data.tsv', 'w')
f.write('%s\n' % '\t'.join(['ID'] + all_meta))
for game_folder in sorted(glob('games/*')):
    serial = game_folder.rstrip('/').split('/')[-1].strip()
    f.write(serial)
    for meta in all_meta:
        f.write('\t')
        meta_fn = '%s/%s.txt' % (game_folder, meta)
        if isfile(meta_fn):
            contents = [v.strip() for v in open(meta_fn).read().strip().splitlines()]
        else:
            contents = list()
        if len(contents) == 0:
            f.write('N/A')
        else:
            f.write(' / '.join(contents))
    f.write('\n')
f.close()
