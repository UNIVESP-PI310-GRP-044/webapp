import logging

import flask
from flask import json, Response
from flask import current_app as app
from sisdiconpra.persistence import db
from sisdiconpra.models.Aluno import Aluno

name = "sisdiconpra.api.v1.alunos"
api = flask.Blueprint(name, __name__)

logger = logging.getLogger(name)

@api.route("/health", methods=["GET"])
def health():
    logger.info("Chamou o /health")
    response = Response(
        response=json.dumps({'mensagem': 'Oi, tudo bem?'}),
        mimetype='application/json',
        status=200,
    )
    return response


@api.route("/", methods=["GET"])
def listar_alunos():
    logger.info("Listando alunos")

    alunos = Aluno.query.all()

    response = Response(
        response=json.dumps({'mensagem': 'Listando Alunos', 'Alunos': [x.json() for x in alunos]} ),
        mimetype='application/json',
        status=200
    )
    return response


@api.route("/", methods=["POST"])
def criar_aluno():
    logger.info("Criando Aluno")

    dados_do_post = flask.request.json
    aluno = Aluno(
        nome_completo=dados_do_post['nome_completo']
    )

    db.session.add(aluno)
    db.session.commit()

    response = Response(
        response=json.dumps({'mensagem': 'Aluno criado!'} ),
        mimetype='application/json',
        status=200
    )
    return response
