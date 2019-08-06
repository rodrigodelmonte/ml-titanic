import joblib
import traceback
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

feature_cols = ['Pclass', 'Parch', 'Age', 'Sex_female', 'Sex_male']


@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        print(json_)
        query = pd.get_dummies(pd.DataFrame(json_))
        query = query.reindex(columns=feature_cols, fill_value=0)
        prediction = list(lr.predict(query))
        return jsonify({'prediction': str(prediction)})
    except Exception:
        return jsonify({'trace': traceback.format_exc()})


if __name__ == '__main__':
    lr = joblib.load("lr_model.pkl")
    app.run(debug=True)
