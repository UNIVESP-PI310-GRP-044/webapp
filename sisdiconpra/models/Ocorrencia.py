from sisdiconpra.persistence import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Ocorrencia(db.Model):
    __tablename__ = 'ocorrencia'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, unique=False)
    id_aluno = db.Column(db.Integer,ForeignKey('aluno.id'))
    aluno = relationship("Aluno", back_populates="ocorrencias")

    def __init__(self, data=data, id_aluno=id_aluno):
        self.data = data
        self.id_aluno = id_aluno

    def __repr__(self):
        return f'<Ocorrencia {self.id_aluno!r}>'

    def json(self):
        return {
            "id": str(self.id),
            "data": self.data,
            "id_aluno": self.id_aluno,
            "aluno": self.aluno.json()
        }