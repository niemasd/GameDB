#! /usr/bin/env python3
'''
Calculate the pairwise edit distances between a bunch of files (e.g. titles)
'''
from multiprocessing import Pool
from os import cpu_count
from os.path import isfile
from sys import stderr
try:
    from tqdm import tqdm
except:
    print("Unable to import tqdm. Install with: pip install tqdm"); exit(1)
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

# parallel helper function
def edit_distance_parallel(x):
    data, fn_s, fn_t, ignore_articles, ignore_case = x
    d = edit_distance(data[fn_s], data[fn_t], ignore_articles=ignore_articles, ignore_case=ignore_case)
    return (d, fn_s, fn_t)

# main program
if __name__ == "__main__":
    # parse user args
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('files', metavar='file.txt', type=str, nargs='+', help="Files to compare")
    parser.add_argument('-o', '--output', type=str, required=False, default='stdout', help="Output file (TSV)")
    parser.add_argument('-oc', '--output_contents', action="store_true", help="Ouput file contents (in addition to just filenames)")
    parser.add_argument('-ia', '--ignore_articles', action="store_true", help="Ignore articles ('The', 'A', and 'An')")
    parser.add_argument('-ic', '--ignore_case', action="store_true", help="Ignore case")
    parser.add_argument('-t', '--threads', type=int, default=cpu_count(), help="Number of Threads")
    parser.add_argument('-cs', '--chunk_size', type=int, default=1024, help="Chunk Size")
    args = parser.parse_args()

    # check user args
    if len(args.files) < 2:
        raise ValueError("Must specify at least 2 files")
    if args.threads < 1 or args.threads > cpu_count():
        raise ValueError("Number of threads must be between 1 and %d: %d" % (cpu_count(), args.threads()))
    if args.chunk_size < 1:
        raise ValueError("Chunk size must be positive: %d" % args.chunk_size)
    for fn in args.files:
        if not isfile(fn):
            raise ValueError("File not found: %s" % fn)
    stderr.write("Loading data from %d files...\n" % len(args.files))
    data = {fn:open(fn).read().strip() for fn in args.files}

    # calculate pairwise edit distances
    num_pairs = len(args.files) * (len(args.files)-1) // 2
    dists = list() # list of (edit_distance, file1, file2) tuples
    inputs = ((data, args.files[i], args.files[j], args.ignore_articles, args.ignore_case) for i in range(0, len(args.files)-1) for j in range(i+1, len(args.files)))
    pool = Pool(processes=args.threads)
    for result in tqdm(pool.imap_unordered(edit_distance_parallel, inputs, chunksize=args.chunk_size), total=num_pairs):
        dists.append(result)
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
