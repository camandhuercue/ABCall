from app import db

class PQR(db.Model):
    __tablename__ = "pqr"
    __table_args__ = {'schema': 'pqrs'}

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Usuario = db.Column(db.String)
    Servicio = db.Column(db.String)
    Estado = db.Column(db.String)
    FechaApertura = db.Column(db.BigInteger)
    FechaCierre = db.Column(db.BigInteger)
    Comentarios = db.Column(db.String)

    def to_dict(self):
        return {
            "id": str(self.Id),
            "usuario": self.Usuario,
            "servicio": self.Servicio,
            "estado": self.Estado,
            "fecha_apertura": str(self.FechaApertura),
            "fecha_cierre": str(self.FechaCierre),
            "comentarios": self.Comentarios
        }

class Comentarios(db.Model):
    __tablename__ = "comentarios"
    __table_args__ = {'schema': 'pqrs'}

    Id = db.Column(db.String, primary_key=True)
    Comentario = db.Column(db.String)
    FechaCreacion = db.Column(db.BigInteger)
    Creador = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.Id,
            "comentario": self.Comentario,
            "fecha_creacion": self.FechaCreacion,
            "creador": self.Creador
        }
