#!/usr/bin/env python3

import json
import re
import glob
from os.path import isfile
from pandas import DataFrame, read_pickle, concat
from lib.yababay.corpus import Ethnical

ethnical_corpus = Ethnical()
ethnical_counts_df = None
ethnical_sents_df  = None

re_filename = re.compile(r'.*\/([^\/]+.txt)$')

CORPUS_DIR = '../assets/corpus'

is_source_dict = None

with open('../frontend/docs/library.json') as f:
    is_source_dict = dict(map(lambda el: (el['sha256'], el['is_source']), json.load(f)))

text_files = [re.match(re_filename, filename).group(1) for filename in glob.glob(f'{CORPUS_DIR}/*.txt')]
for filename in text_files:
    pickle_filename = f'{CORPUS_DIR}/{filename.replace(".txt", "-ethnical.pkl")}'
    if isfile(pickle_filename):
        df = read_pickle(pickle_filename)
        fn = filename.replace('.txt', '')
        df['filename']  = [fn, fn]
        df['is_source'] = is_source_dict[fn]
        if ethnical_counts_df is None:
            ethnical_counts_df = df.iloc[[0]]
            ethnical_sents_df  = df.iloc[[1]]
        else:
            ethnical_counts_df = concat([ethnical_counts_df, df.iloc[[0]]])
            ethnical_sents_df  = concat([ethnical_sents_df,  df.iloc[[1]]])
        print(f'Joined: {filename}')
        continue
    print(f'Parsing {filename}...')
    df = DataFrame(ethnical_corpus.parse_book(filename))
    df.to_pickle(pickle_filename)

print(ethnical_counts_df.shape)
print(ethnical_sents_df.shape)
ethnical_counts_df.set_index('filename', inplace=True)
ethnical_sents_df.set_index('filename', inplace=True)
ethnical_counts_df.to_pickle('../assets/analitics/ethnical-counts.pkl')
ethnical_sents_df.to_pickle('../assets/analitics/ethnical-sents.pkl')

