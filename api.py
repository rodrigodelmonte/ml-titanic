import os
from flask import Flask
from flask_restplus import Resource, Api, fields
from model import Model

app = Flask(__name__)

api = Api(app, version='1.0', title='Titanic API',
          description='A simple Titanic API to preditct survivers')

ns = api.namespace('titanic', description='Predict Titanic survivers')


features = api.model('features', {
    'Pclass': fields.Integer(required=True,
                             description='Ticket class',
                             example=3),
    'Parch': fields.Integer(required=True,
                            description='parents/children aboard the Titanic',
                            example=0),
    'Age': fields.Integer(required=True, description='Age', example=33),
    'Sex': fields.String(required=True, description='Sex', example='female')
})

clf = Model()

@api.route('/predict')
class Predict(Resource):

    @ns.doc('predict')
    @ns.expect(features)
    @ns.response(200, '0 or 1')
    def post(self):

        return clf.predict([api.payload])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
