This directory contains helper scripts.

# `edit_distance.py`
Calculate the pairwise edit distances between a bunch of files (e.g. titles).

# `parse_filename.py`
Parse a filename to extract the title, region, language(s), etc. and print as TSV.

# `rename_regions.py`
Rename regions to be NTSC-U, NTSC-PAL, or NTSC-J.

# `scrape_redump.py`
Scrape metadata from a Redump URL.

# `search_mobygames.py`
Search MobyGames for a given game.

## Bulk-add missing release dates

```bash
for serial in $(echo $(ls && ls */release_date.txt) | tr ' ' '\n' | cut -d'/' -f1 | sort | uniq -c | rev | cut -d' ' -f1-2 | rev | grep -v "^2 " | cut -d' ' -f2) ; do echo -n "$serial " && cat $serial/title.txt && ~/GameDB/helper/search_mobygames.py -k <MOBY_API_KEY> -t "$(cat $serial/title.txt)" -p <CONSOLE> | cut -f2 | grep -v "^Release Date" | head -1 > $serial/release_date.txt && sleep 1.5 ; done
```
