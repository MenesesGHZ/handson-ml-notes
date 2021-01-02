'''
    Code Recovered from `Hands-On Machine Learning with ScikitLearn and TensorFlow` by Aurélien Géron. 
    Chapter #2 Pag.44 
'''

import os
import tarfile
import pandas as pd
from six.moves import urllib

DOWNLOAD_ROOT = "https://github.com/ageron/handson-ml/blob/master/datasets/housing/housing.tgz?raw=true"
HOUSING_PATH = "dataset/"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    print("\n* DOWNLOADING DATA...")
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    print("* EXTRACTING DATA...")
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    print("* Finished\n")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

