from .models import Usuarios
from ariadne import convert_kwargs_to_snake_case

def getUsers_resolver(obj, info):
    try:
        usuario = [usuario.to_dict() for usuario in Usuarios.query.all()]
        payload = {
            "success": True,
            "usuarios": usuario
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

def getUser_resolver(obj, info, user):
    try:
        usuario = [usuario.to_dict() for usuario in Usuarios.query.filter_by(Id=int(user)).all()]
        payload = {
            "success": True,
            "usuario": usuario
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
