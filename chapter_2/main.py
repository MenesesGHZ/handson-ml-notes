import argparse 
from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV
from data_loader import fetch_housing_data, load_housing_data 


def main(download_data):
    # Download data
    if download_data:
        fetch_housing_data()
    
    # Load data
    dataset = load_housing_data()
    
    # Plotting data for visualization
    print(dataset.columns)
    print(dataset.corr())

    # Preprocessing data
    #pipeline = load_pipeline()


    # SVM as a regresor model
    #support_vector_machine_reg = SVR()

    # 
    #randomized_search = RandomizedSearchCV(support_vector_machine_reg,cv=10,scoring="neg_mean_squared_error")


    # Fitting SVM model
    #randomized_search.fit()





if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('--download-data', dest='download_data', action='store_true')
    parser.add_argument('--no-download-data', dest='download_data', action='store_false')
    parser.set_defaults(download_data=True)
    args = parser.parse_args()
    main(download_data=args.download_data)
