from sisdiconpra.persistence import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from base64 import b64encode
class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(150))
    foto = db.Column(db.LargeBinary)

    ocorrencias = relationship("Ocorrencia", back_populates="aluno")

    def __init__(self, nome_completo=None, foto=None):
        self.nome_completo = nome_completo
        self.foto = foto

    def __repr__(self):
        return f'<Aluno {self.nome_completo!r}>'

    def json(self):
        return {
            "id": str(self.id),
            "nome_completo": self.nome_completo,
            "foto": b64encode(self.foto).decode('utf-8') if self.foto else None
        }
