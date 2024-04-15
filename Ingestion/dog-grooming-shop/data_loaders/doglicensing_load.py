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

    In this case loading the data from my repository
    Specifically for the Dog Licensing Dataset
    
    """
    
    
    url = 'https://github.com/juangrau/project/raw/master/EDA/NYC_Dog_Licensing_Dataset_20240411.csv'
    response = requests.get(url)

    # As previously identified on the EDA these are the columns that have date values
    parse_dates = ['LicenseIssuedDate', 'LicenseExpiredDate']


    dog_licensing_dtypes = {
        'AnimalName': str, 
        'AnimalGender': str, 
        'AnimalBirthYear': int, 
        'BreedName': str, 
        'ZipCode': int,
        'Extract Year': int 
    }

    df = pd.read_csv(io.StringIO(response.text), sep=',', parse_dates=parse_dates, dtype=dog_licensing_dtypes)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
