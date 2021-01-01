from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, LabelBinarizer
from sklearn.base import BaseEstimator, TransformerMixin


# Select specific attributes among data to apply to them the next transformations in the pipeline 
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    
    def fit(self, X, y=None):
        return self


def load_pipeline(numerical_attributes,categorical_attributes,imputer_strategy="median",scaler_range=(0,1)):
    # Pipeline for numerical attributes
    numerical_pipeline = Pipeline([
            ("selector", DataFrameSelector(numerical_attributes)),
            ("imputer",Imputer(strategy=imputer_strategy)),
            ("scaler",MinMaxScaler(feature_range=scaler_range))
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
