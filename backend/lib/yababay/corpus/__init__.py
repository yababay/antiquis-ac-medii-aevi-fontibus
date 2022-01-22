from nltk.data import LazyLoader
from nltk.corpus import PlaintextCorpusReader
from .ethnical import EthnicalTokenizer


class Corpus(PlaintextCorpusReader):
    def __init__ (self, tokenizers: dict):
        CORPUS_DIRECTORY = '../assets/corpus'
        super().__init__(CORPUS_DIRECTORY, r'.*\.txt$', encoding = 'utf-8', 
                sent_tokenizer = LazyLoader('tokenizers/punkt/PY3/russian.pickle'))
        self.tokenizers = tokenizers


    def parse_book(self, path):
        series = {} 
        for item, reg in list(self.tokenizers.items()):
            series[item] = self.get_frequency(reg, path)
        return series


    def get_frequency(self, reg, path):
        sents = self.sents(path)
        count = 0
        indexes = []
        for i, sent in enumerate(sents):
            cnt = len(reg.tokenize(' '.join(sent)))
            if cnt > 0:
                indexes.append(i)
                count += cnt
        return {"count": count, "sents": indexes}


    def get_sentence(self, path, n):
        return self.sent_to_string(self.sents(path)[n])

    @property
    def columns(self):
        return list(self.tokenizers.keys())

    @property
    def statistics(self):
        freq = {}
        for item, reg in list(self.tokenizers.items()):
            freq[item] = {}
            for path in self.fileids():
                path_key = path.replace('.txt', '')
                try:
                    freq[item][path_key] = self.get_frequency(reg, path)
                except AssertionError:
                    print(f'Assertion error in {path}.')
        return freq


    @classmethod
    def sent_to_string(cls, sent):
        text = ' '.join(sent)
        for ch in r'\"\'\.\,\!\?\»\:\;':
            text = text.replace(f' {ch}', ch) 
        text.replace('« ', '«')
        return text


class Ethnical(Corpus):

    def __init__(self):
        super().__init__(EthnicalTokenizer.all())

