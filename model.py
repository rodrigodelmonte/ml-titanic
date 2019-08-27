import joblib
import pandas as pd


class Model(object):

    def __init__(self):

        self.features = joblib.load('../model/features.pkl')
        self.clf = joblib.load("../model/lr_model.pkl")

    def pipeline(self, X):

        _X = pd.get_dummies(pd.DataFrame(X), columns=['Sex'])
        _X = _X.reindex(columns=self.features, fill_value=0)
        return _X

    def predict(self, X):
        _X = self.pipeline(X)
        result = int(self.clf.predict(_X))
        return result
