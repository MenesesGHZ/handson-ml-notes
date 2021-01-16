from scipy import stats
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, LabelBinarizer
from sklearn.base import BaseEstimator, TransformerMixin

# Select specific attributes among data to apply to them the next transformations in the pipeline 
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


# Select the variables that has the strongest correlation with the response.
class CorrelationFilter(BaseEstimator, TransformerMixin):
    def __init__(self,numerical_attr,response_attr,coef_criterium): # no *args or **kargs
        if response_attr in numerical_attr:
            numerical_attr.remove(response_attr)
        self.numerical_attr = numerical_attr 
        self.response_attr = response_attr
        self.coef_criterium = coef_criterium

    def fit(self, X, y=None):
        return self # nothing else to do
    
    def transform(self, X, y=None):
        selected_attr = [self.response_attr]
        # Selecting features with a spearman correlation higher than `self.coef_criterium`
        for attr in self.numerical_attr:
            coef = stats.spearmanr(X[attr],X[self.response_attr])[0]
            if coef > abs(self.coef_criterium):
                selected_attr.append(attr)
        return X[selected_attr]

def load_pipeline(numerical_attributes,categorical_attributes,response_attribute,imputer_strategy="median",scaler_range=(0,1),coef_criterium=0.2):
    # Pipeline for numerical attributes
    numerical_pipeline = Pipeline([
            ("selector", DataFrameSelector(numerical_attributes)),
            ("imputer",SimpleImputer(strategy=imputer_strategy)),
            ("scaler",MinMaxScaler(feature_range=scaler_range)),
            ("corr_filter",CorrelationFilter(numerical_attributes,response_attribute,coef_criterium))
            ])

    # Pipeline for categorical attributes
    categorical_pipeline = Pipeline([
            ("selector", DataFrameSelector(categorical_attributes)),
            ("binarizer",LabelBinarizer())
            ])

    # Concatenating numerical and categorical pipelines
    full_pipeline = FeatureUnion([
            ("numerical_pipeline",numerical_pipeline),
            ("categorical_pipeline",categorical_pipeline)
        ])

    return full_pipeline
