#!/usr/bin/env python3

import re
import glob
from numpy import nan
from os.path import isfile
from pandas import DataFrame, read_pickle, concat
from lib.yababay.corpus import Ethnical

ethnical_corpus = Ethnical()
ethnical_df = None

re_filename = re.compile(r'.*\/([^\/]+.txt)$')

CORPUS_DIR = '../assets/corpus'

text_files = [re.match(re_filename, filename).group(1) for filename in glob.glob(f'{CORPUS_DIR}/*.txt')]
for filename in text_files:
    pickle_filename = f'{CORPUS_DIR}/{filename.replace(".txt", "-ethnical.pkl")}'
    if isfile(pickle_filename):
        print('ok', filename)
        df = read_pickle(pickle_filename)
        df['filename'] = [filename.replace('.txt', '_count'), filename.replace('.txt', '_sents')]
        if ethnical_df is None:
            ethnical_df = df
        else:
            ethnical_df = concat([ethnical_df, df])
        continue
    print(filename)
    df = DataFrame(ethnical_corpus.parse_book(filename))
    df.to_pickle(pickle_filename)

if ethnical_df is not None:
    print(ethnical_df.shape)
    ethnical_df.set_index('filename', inplace=True)
    ethnical_df.to_pickle('../assets/analitics/ethnical.pkl')

