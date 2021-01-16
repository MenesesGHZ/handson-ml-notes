import argparse
from plotter import plot_housing_data
from sklearn.svm import SVR
from sklearn.model_selection import RandomizedSearchCV
from data_loader import fetch_housing_data, load_housing_data 
from preprocess import load_pipeline

def main(download_data):
    # Download data
    if download_data:
        fetch_housing_data()
    
    # Load data
    dataset = load_housing_data()
    numerical_attr = ["median_income","total_bedrooms","total_rooms","housing_median_age","households","population","longitude","latitude"]
    categorical_attr = ["ocean_proximity"]
    response_attr = "median_house_value"

    #Dividing dataset into X,y
    X = dataset[numerical_attr+categorical_attr]
    y = dataset[response_attr]
    
    # Plotting data for visualization
  #  pairplot_attributes = ["median_house_value", "median_income", "total_rooms","housing_median_age"]
  #  plot_housing_data(dataset,pairplot_attributes) 
        
    # Loading Pipeline to preprocess data
    pipeline = load_pipeline(numerical_attr,categorical_attr,response_attr)
    
    # Preprocessing data
    pipeline.fit(X,y)
    print(housing_prepared)

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
