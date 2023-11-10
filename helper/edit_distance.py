#! /usr/bin/env python3
'''
Calculate the pairwise edit distances between a bunch of files (e.g. titles)
'''
from os.path import isfile
from sys import stderr
import argparse
ARTICLE_PREFIXES = ['THE ', 'A ', 'AN ']

# calculate edit distance between s and t
def edit_distance(s, t, ignore_articles=False, ignore_case=False):
    # preprocess strings if needed
    if args.ignore_case:
        s = s.upper(); t = t.upper()
    if args.ignore_articles:
        s_up = s.upper(); t_up = t.upper()
        for prefix in ARTICLE_PREFIXES:
            if s_up.startswith(prefix):
                s_up = s_up[len(prefix):]; s = s[len(prefix):]
            if t_up.startswith(prefix):
                t_up = t_up[len(prefix):]; t = t[len(prefix):]

    # calculate edit distance
    D = [[None for __ in range(len(t)+1)] for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        D[i][0] = i
    for j in range(len(t)+1):
        D[0][j] = j
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                curr = 0
            else:
                curr = 1 # substitutions have a cost of 1 (not 2)
            D[i][j] = min(
                D[i-1][j] + 1,
                D[i][j-1] + 1,
                D[i-1][j-1] + curr,
            )
    return D[-1][-1]

# main program
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', metavar='file.txt', type=str, nargs='+', help="Files to compare")
    parser.add_argument('-o', '--output', type=str, required=False, default='stdout', help="Output file (TSV)")
    parser.add_argument('-oc', '--output_contents', action="store_true", help="Ouput file contents (in addition to just filenames)")
    parser.add_argument('-ia', '--ignore_articles', action="store_true", help="Ignore articles ('The', 'A', and 'An')")
    parser.add_argument('-ic', '--ignore_case', action="store_true", help="Ignore case")
    parser.add_argument('-ld', '--load_data', action="store_true", help="Load all data up-front (faster, but more memory)")
    args = parser.parse_args()

    # check user args
    if len(args.files) < 2:
        raise ValueError("Must specify at least 2 files")
    for fn in args.files:
        if not isfile(fn):
            raise ValueError("File not found: %s" % fn)

    # load data up front if user asks for it
    if args.load_data:
        stderr.write("Loading data from %d files...\n" % len(args.files))
        data = {fn:open(fn).read().strip() for fn in args.files}
    else:
        data = None

    # calculate pairwise edit distances
    num_pairs = len(args.files) * (len(args.files)-1) // 2
    dists = list() # list of (edit_distance, file1, file2) tuples
    for i in range(0, len(args.files)-1):
        if data is None:
            s = open(args.files[i]).read().strip()
        else:
            s = data[args.files[i]]
        for j in range(i+1, len(args.files)):
            stderr.write('Performing comparision %d of %d...\r' % (len(dists)+1, num_pairs)); stderr.flush()
            if data is None:
                t = open(args.files[j]).read().strip()
            else:
                t = data[args.files[j]]
            d = edit_distance(s, t, ignore_articles=args.ignore_articles, ignore_case=args.ignore_case)
            dists.append((d, args.files[i], args.files[j]))
    stderr.write('Successfully performed %d pairwise edit distance calculations\n' % len(dists))

    # write output
    stderr.write("Sorting pairwise edit distances...\n")
    dists.sort()
    stderr.write("Writing pairwise edit distances to: %s\n" % args.output)
    if args.output.strip().lower() == 'stdout':
        from sys import stdout as out_f
    elif isfile(args.output):
        raise ValueError("Output file exists: %s" % args.output)
    else:
        out_f = open(args.output, 'w')
    out_f.write('Edit Distance\tFile 1\tFile 2')
    if args.output_contents:
        out_f.write('\tContents 1\tContents 2')
    out_f.write('\n')
    for d, fn_s, fn_t in dists:
        out_f.write('%d\t%s\t%s' % (d, fn_s, fn_t))
        if args.output_contents:
            if data is None:
                s = open(fn_s).read().strip(); t = open(fn_t).read().strip()
            else:
                s = data[fn_s]; t = data[fn_t]
            out_f.write('\t%s\t%s' % (s, t))
        out_f.write('\n')
    out_f.close()
