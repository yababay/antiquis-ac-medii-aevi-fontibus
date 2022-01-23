import pandas as pd
from .corpus import Corpus

ethnical_counts_df = pd.read_pickle('../assets/analitics/ethnical-counts.pkl')
ethnical_sents_df = pd.read_pickle('../assets/analitics/ethnical-sents.pkl')


def ethnical_count(source_id):
    reply = ethnical_counts_df.loc[[source_id]]
    reply = [(key, value) for key, value in reply.to_dict('list').items() if value[0] > 0]
    return sorted(reply, key=lambda el: el[1][0], reverse=True)


def ethnical_sents(source_id, ethnos):
    sent_nums = ethnical_sents_df.at[source_id, ethnos]
    corpus = Corpus({})
    sents = corpus.sents(source_id + '.txt')
    result = []
    for i, sent in enumerate(sents):
        if i in sent_nums:
            result.append(f'__&sect;{i}__.&nbsp;{Corpus.sent_to_string(sent)}')
    return '\n\n'.join(result)
    
