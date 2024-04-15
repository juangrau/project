import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    
    print(f'Preprocessing: The number of rows is {len(data)}')

    data =  data[data['BreedName'].str.contains('Mix')==False]

    print(f'Preprocessing: The final number of rows is {len(data)}')

    return data


