from api import app, db

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType

from flask import request, jsonify
from api.queries import getUsers_resolver, getUser_resolver

import sys
from datetime import datetime

query = ObjectType("Query")
query.set_field("listUsers", getUsers_resolver)
query.set_field("getUsers", getUser_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

@app.route("/usuarios/graphql", methods=["POST"])
def graphql_server():
    json_data = request.get_json(force=True)
    headers = dict(request.headers)
    RequestId = headers['X-Request-Id']

    print('{} - Inicio de solicitud. Header: {}'.format(datetime.now(), RequestId), file=sys.stderr)

    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400

    print('{} - Fin de solicitud.'.format(datetime.now()), file=sys.stderr)

    return jsonify(result), status_code
