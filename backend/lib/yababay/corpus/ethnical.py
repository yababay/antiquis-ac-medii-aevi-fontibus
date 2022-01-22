from yaml import load, FullLoader
from nltk.tokenize import RegexpTokenizer

class EthnicalTokenizer(RegexpTokenizer):


    def __init__(self, pattern: str):
        f = pattern[0]
        self.pattern = f' ({f.upper()}|{f}){pattern[1:]}[^а-я]'.replace('*', '|ам|ами|ах')
        super().__init__(self.pattern)


    def __str__(self):
        word = self.pattern[4:].lower().replace(')', '')
        if '(' not in word:
            return word
        n = word.index('(') + 2
        return word[:n].replace('(', '')

    @classmethod
    def all(cls):
        with open('../assets/aspects/ethnical.yaml', 'r') as file:
            ethnoses = {}
            for ethnos in load(file, FullLoader):
                ethnical = EthnicalTokenizer(ethnos)
                ethnoses[str(ethnical)] = ethnical    
            return ethnoses

