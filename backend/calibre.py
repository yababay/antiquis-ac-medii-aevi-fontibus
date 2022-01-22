#!/usr/bin/env calibre-debug

import re
import json
from os.path import isfile

from calibre.library import db

LIBRARY_PATH = '/home/yababay/public/calibre/history'

re_year = re.compile(r'\d+')
re_era  = re.compile(r'.*до\s+н\.(\s+)?э\..*', re.MULTILINE)

db = db(LIBRARY_PATH, read_only=True).new_api
sorted_authors = {}

for author in db.author_data().values():
    sorted_authors[author['name']] = author['sort'] 

books = []
for book_id in db.books_in_virtual_library('Antiquis ac medii aevi fontibus'):
    fields = {}
    for field in ['authors', 'title', 'comments']:
        fields[field] = db.field_for(field, book_id)
    tags = db.field_for('tags', book_id)
    sha256 = db.format_hash(book_id, 'txt')
    is_source = 'источник' in tags
    fields['sorted_author'] = sorted_authors[fields['authors'][0]]
    fields['authors'] = ', '.join(fields['authors'])
    fields['is_source'] = is_source
    fields['sha256'] = sha256
    comments = fields['comments']
    if is_source and comments:
        comments = fields['comments'].strip().replace('\n', '')
        years = [int(year) for year in re.findall(re_year, comments)]
        year = 1000 if not years else max(years)
        era_is_negative = re.match(re_era, comments)
        if era_is_negative:
            year = 0 - year
        fields['year'] = year
    books.append(fields)
    file_name = f'../assets/corpus/{sha256}.txt'
    if not isfile(file_name):
        print(sha256)
        db.copy_format_to(book_id, 'txt', file_name)

books = sorted(books, key=lambda el: (el['sorted_author'], el['title']))

with open('../frontend/docs/library.json', 'w') as fn:
    fn.write(json.dumps(books, ensure_ascii=False))
    print(f'Импортировано {len(books)} текстов.')

