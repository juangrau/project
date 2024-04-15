import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/juangrau/project/raw/master/datafiles/akc-data-latest.csv'
    response = requests.get(url)

    # As previously identified on the EDA these are dtypes of the columns for this dataset

    dog_breeds_dtypes = {
        'breed_name': str,
        'description': str,
        'temperament': str,
        'popularity': str,
        'min_height': float,
        'max_height': float,
        'min_weight': float,
        'max_weight': float,
        'min_expectancy': float,
        'max_expectancy': float,
        'group': str,
        'grooming_frequency_value': float,
        'grooming_frequency_category': str,
        'shedding_value': float,
        'shedding_category': str,
        'energy_level_value': float,
        'energy_level_category': str,
        'trainability_value': float,
        'trainability_category': str,
        'demeanor_value': float,
        'demeanor_category': str
    }

    df = pd.read_csv(io.StringIO(response.text), sep=',', dtype=dog_breeds_dtypes)
    return df



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
