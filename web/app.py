from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json
import requests
import sys
from datetime import datetime

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

graphql_query_user = """{{
    getUsers(user: "{}") {{
        success
        errors
        usuario {{
            id
            usuario
            servicios
            telefono
            correo
            prestadora_servicio
            empresa
        }}
    }}
}}"""

class QueryData(Resource):
    def get(self):
        return {"status": "OK"}, 200

    def post(self):
        json_data = request.get_json(force=True)
        headers = dict(request.headers)
        RequestId = headers['X-Request-Id']

        print('{} - Inicio de solicitud. Header: {}'.format(datetime.now(), RequestId), file=sys.stderr)

        print('{} - Consultando servicio de incidentes. Tabla de Incidentes'.format(datetime.now()), file=sys.stderr)

        data = {'query': graphql_query_incidents.format(json_data['user']['id'])}
        query_incidents = requests.post(url="http://graphql:5000/graphql", data=json.dumps(data), headers={"Content-Type": "application/json", "X-Request-Id": RequestId})

        print('{} - Fin solicitud servicio de incidentes. Tabla de Incidentes'.format(datetime.now()), file=sys.stderr)

        incidentes = []
        for incidente in query_incidents.json()['data']['getPQR']['pqrs']:

            print('{} - Consultando servicio de incidentes. Tabla de Comentarios. Comentario(s) {}'.format(datetime.now(), incidente['comentarios']), file=sys.stderr)

            data = {'query': graphql_query_comments.format(incidente['comentarios'])}
            query_comments = requests.post(url="http://graphql:5000/graphql", data=json.dumps(data), headers={"Content-Type": "application/json", "X-Request-Id": RequestId})
            incidentes.append({'id': incidente['id'], 'data': query_comments.json()['data']['getComments']['comentarios']})

        print('{} - Fin solicitud servicio de incidentes. Tabla de Comentarios'.format(datetime.now()), file=sys.stderr)

        print('{} - Consultando servicio de Usuarios. Tabla de Usuarios'.format(datetime.now()), file=sys.stderr)

        data = {'query': graphql_query_user.format(json_data['user']['id'])}
        query_usuario = requests.post(url="http://usuarios:5000/usuarios/graphql", data=json.dumps(data), headers={"Content-Type": "application/json", "X-Request-Id": RequestId})

        print('{} - Fin solicitud servicio de Usuarios. Tabla de Usuarios'.format(datetime.now()), file=sys.stderr)

        resp = {'headers': headers, 'json': json_data, 'prqs': query_incidents.json()['data']['getPQR']['pqrs'], 'incidentes': incidentes, 'usuario': query_usuario.json()['data']['getUsers']['usuario']}
        return resp, 201

api.add_resource(QueryData, '/web')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
