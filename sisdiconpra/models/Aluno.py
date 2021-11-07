from sisdiconpra.persistence import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Aluno(db.Model):
    __tablename__ = 'aluno'
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(150))

    ocorrencias = relationship("Ocorrencia", back_populates="aluno")

    def __init__(self, nome_completo):
        self.nome_completo = nome_completo

    def __repr__(self):
        return f'<Aluno {self.nome_completo!r}>'

    def json(self):
        return {
            "id": str(self.id),
            "nome_completo": self.nome_completo
        }