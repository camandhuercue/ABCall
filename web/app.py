from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json
import requests

app = Flask(__name__)
api = Api(app)

graphql_query_incidents = """{{
    getPQR(user: "{}") {{
        success
        errors
        pqrs {{
            id
            usuario
            servicio
            estado
            fecha_apertura
            fecha_cierre
            comentarios
        }}
    }}
}}"""

graphql_query_comments = """{{
    getComments(id: "{}") {{
        success
        errors
        comentarios {{
            id
            comentario
            fecha_creacion
            creador
        }}
    }}
}}"""

class QueryData(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        headers = dict(request.headers)
        data = {'query': graphql_query_incidents.format(json_data['user']['id'])}
        query_incidents = requests.post(url="http://graphql:5000/graphql", data=json.dumps(data), headers={"Content-Type": "application/json"})
        incidentes = []
        for incidente in query_incidents.json()['data']['getPQR']['pqrs']:
            data = {'query': graphql_query_comments.format(incidente['comentarios'])}
            query_comments = requests.post(url="http://graphql:5000/graphql", data=json.dumps(data), headers={"Content-Type": "application/json"})
            incidentes.append({'id': incidente['id'], 'data': query_comments.json()['data']['getComments']['comentarios']})

        resp = {'headers': headers, 'json': json_data, 'graphql': query_incidents.json(), 'incidentes': incidentes}
        return resp, 201

api.add_resource(QueryData, '/web')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
