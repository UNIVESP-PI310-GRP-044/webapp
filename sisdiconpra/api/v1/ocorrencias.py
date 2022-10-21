import logging

import flask
from flask import json, Response
from flask import current_app as app
from sisdiconpra.persistence import db
from sisdiconpra.models.Ocorrencia import Ocorrencia
from sisdiconpra.models.Aluno import Aluno
import datetime

name = "sisdiconpra_api_v1_ocorrencias"
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
def listar_ocorrencias():
    logger.info("Listando ocorrencias")

    ocorrencias = Ocorrencia.query.all()

    response = Response(
        response=json.dumps({'mensagem': 'Listando Ocorrencias', 'Ocorrencias': [x.json() for x in ocorrencias]} ),
        mimetype='application/json',
        status=200
    )
    return response

@api.route("/", methods=["POST"])
def criar_ocorrencias():
    logger.info("Listando ocorrencias")

    dados_do_post = flask.request.json
    ocorrencia = Ocorrencia(
        data=datetime.datetime.utcnow().replace(tzinfo=None).replace(microsecond=0),
        id_aluno=dados_do_post['id_aluno']
    )

    db.session.add(ocorrencia)
    db.session.commit()


    response = Response(
        response=json.dumps({'mensagem': 'Ocorrencia criada!'} ),
        mimetype='application/json',
        status=200
    )
    return response
