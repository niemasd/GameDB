#! /usr/bin/env python3
'''
Add a prefix string to the beginning of a file if it doesn't already have it
'''
from sys import argv, stderr

# main program
if __name__ == "__main__":
    if len(argv) != 3:
        print("USAGE: %s <prefix> <filename>" % argv[0], file=stderr); exit(1)
    with open(argv[2], 'rt') as f:
        s = f.read().strip()
    if not s.startswith(argv[1]):
        with open(argv[2], 'wt') as f:
            f.write('%s%s\n' % (argv[1], s))
