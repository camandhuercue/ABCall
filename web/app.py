from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json
import requests

app = Flask(__name__)
api = Api(app)

graphql_query = """{
    listPQR {
        success
        errors
        pqrs {
            id
            usuario
        }
    }
}"""

#parser = reqparse.RequestParser()
#parser.add_argument('user', location='json')

class TodoList(Resource):
    def get(self):
        args = parser.parse_args()
        print(args)
        return dict(request.headers)

    def post(self):
#        args = parser.parse_args()
        json_data = request.get_json(force=True)
        headers = dict(request.headers)
        data = {'query': graphql_query}
        query = requests.post(url="http://graphql:5000/graphql", data=json.dumps(data), headers={"Content-Type": "application/json"})
        resp = {'headers': headers, 'json': json_data, 'graphql': query.json()}
        return resp, 201

api.add_resource(TodoList, '/app1/todos')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
