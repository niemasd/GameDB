#! /usr/bin/env python3
'''
Scrape metadata from a Redump URL
'''
from bs4 import BeautifulSoup
from os import makedirs
from sys import argv
from urllib.request import urlopen

# clean a string
def clean(s):
    return s.replace(chr(65533),'').replace(chr(0),'').replace(u'\xa0 ',u' ').replace(u'\xa0',u' ').strip()

# main program
if __name__ == "__main__":
    if len(argv) == 1 or argv[1].lower() in {'-h', '--help', '-help'}:
        print("USAGE: %s <redump_url> [redump_url_2] [redump_url_3] [...]" % argv[0]); exit(1)
    for url in argv[1:]:
        print("Parsing: %s" % url)
        soup = BeautifulSoup(urlopen(url).read(), 'html.parser')
        for table in soup.find_all('table', {'class': 'games'}):
            for row in table.find_all('tr'):
                cols = list(row.find_all('td'))
                if len(cols) == 0:
                    continue
                # parse/clean attributes
                region, title, system, version, edition, languages, serial, status = cols
                region = clean(list(region.find_all('img'))[0]['title'])
                title = clean(title.get_text(separator='\n').splitlines()[0])
                system = clean(system.text)
                version = clean(version.text)
                edition = clean(edition.text)
                languages = [clean(v['title']) for v in languages.find_all('img')]
                try:
                    serials = clean(serial['title']).split(', ')
                except:
                    serials = clean(serial.text).split(', ')
                serials = [clean(v).replace(' ','-').replace('/','-') for v in serials if len(v) != 0]
                status = clean(list(status.find_all('img'))[0]['title'])

                # write attributes to files
                for serial in serials:
                    makedirs(serial, exist_ok=True)
                    if len(region) != 0:
                        f = open('%s/region.txt' % serial, 'w'); f.write('%s\n' % region); f.close()
                    if len(title) != 0:
                        f = open('%s/title.txt' % serial, 'w'); f.write('%s\n' % title); f.close()
                    if len(system) != 0:
                        f = open('%s/system.txt' % serial, 'w'); f.write('%s\n' % system); f.close()
                    if len(version) != 0:
                        f = open('%s/version.txt' % serial, 'w'); f.write('%s\n' % version); f.close()
                    if len(edition) != 0:
                        f = open('%s/edition.txt' % serial, 'w'); f.write('%s\n' % edition); f.close()
                    if len(languages) != 0:
                        f = open('%s/language.txt' % serial, 'w'); f.write('%s\n' % '\n'.join(languages)); f.close()
                    if len(status) != 0:
                        f = open('%s/redump_status.txt' % serial, 'w'); f.write('%s\n' % status); f.close()
