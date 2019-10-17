import os
import connexion
from flask import request
from model import Model


clf = Model()

def predict():
    body = request.json
    return clf.predict([body])

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('openapi.yaml')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=os.environ.get('PORT', 5000))
