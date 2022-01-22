import pandas as pd

ethnical_df = pd.read_pickle('../assets/analitics/ethnical.pkl')

def ethnical_by_source(source_id):
    reply = ethnical_df.loc[[f'{source_id}_count',  f'{source_id}_sents']]
    reply = [(key, value) for key, value in reply.to_dict('list').items() if value[0] > 0]
    return sorted(reply, key=lambda el: el[1][0], reverse=True)
    
