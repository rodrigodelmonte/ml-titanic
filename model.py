import joblib
import pandas as pd


class Model(object):

    def __init__(self):

        self.features = joblib.load('features.pkl')
        self.clf = joblib.load('logreg_model.pkl')

    def pipeline(self, X):
        '''
        Transform Sex fetature to a dummy indicattor
        Ex: Sex=female or Sex=male to Sex_female=1 or Sex_male=1
        '''

        _X = pd.get_dummies(pd.DataFrame(X), columns=['Sex'])
        _X = _X.reindex(columns=self.features, fill_value=0)
        return _X

    def predict(self, X):

        _X = self.pipeline(X)
        prediction = int(self.clf.predict(_X))
        return prediction
