from app import db

class Usuarios(db.Model):
    __tablename__ = "usuarios"
    __table_args__ = {'schema': 'usuarios'}

    Id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Usuario = db.Column(db.String)
    Servicios = db.Column(db.String)
    Telefono = db.Column(db.String)
    Correo = db.Column(db.String)
    PrestadoraServicio = db.Column(db.String)
    Empresa = db.Column(db.String)

    def to_dict(self):
        return {
            "id": str(self.Id),
            "usuario": self.Usuario,
            "servicios": self.Servicios,
            "telefono": self.Telefono,
            "correo": self.Correo,
            "prestadora_servicio": self.PrestadoraServicio,
            "empresa": self.Empresa
        }
