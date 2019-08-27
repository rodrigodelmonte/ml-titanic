import traceback
from flask import Flask, request, jsonify, make_response
from flask_restful import Api
from flask_restful import Resource
from model import Model

app = Flask(__name__)
api = Api(app)
clf = Model()


class Predict(Resource):

    def post(self):
        try:
            json_ = request.get_json(force=True)
            predict = clf.predict(json_['features'])
            return make_response(jsonify(prediction=predict), 200)
        except Exception:
            return make_response(jsonify(error=traceback.format_exc()), 500)


api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
