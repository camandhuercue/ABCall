from .models import PQR, Comentarios
from ariadne import convert_kwargs_to_snake_case
from sqlalchemy import or_

def listPQR_resolver(obj, info):
    print("algo")
    try:
        pqrs = [pqr.to_dict() for pqr in PQR.query.all()]
        print(pqrs)
        payload = {
            "success": True,
            "pqrs": pqrs
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload

@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, user):
    try:
        pqrs = [pqr.to_dict() for pqr in PQR.query.filter_by(Usuario=str(user)).all()]
        print(pqrs)
        payload = {
            "success": True,
            "pqrs": pqrs
        }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

def getComment_resolver(obj, info, id):
    try:
        if ";" in id:
            ids = id.split(";")
            comments = []
            for i in ids:
                comment = Comentarios.query.get(i)
                comments.append(comment.to_dict())
            #comments = [comment.to_dict() for comment in Comentarios.query.filter_by(or_(Id == v for v in ids)).all()]
            print(comments)
            payload = {
                "success": True,
                "comentarios": comments
            }
        else:
            comments = [comment.to_dict() for comment in Comentarios.query.filter_by(Id = id).all()]
            print(comments)
            payload = {
                "success": True,
                "comentarios": comments
            }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload
