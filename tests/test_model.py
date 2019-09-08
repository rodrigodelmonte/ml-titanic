def test_pipeline(model):

    payload = [{"Pclass": 3, "Parch": 0, "Age": 22, "Sex": "male"}]
    features = model.pipeline(payload)
    features = features.to_dict()
    assert 'Pclass' in features
    assert 'Parch' in features
    assert 'Age' in features
    assert 'Sex_male' in features
    assert 'Sex_female' in features

def test_predict(model):

    payload = [{"Pclass": 3, "Parch": 0, "Age": 22, "Sex": "male"}]
    predict = model.predict(payload)
    assert type(predict) == int
    assert predict in [0, 1]
