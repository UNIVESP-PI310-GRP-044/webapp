import logging

import flask
from flask import json, Response
from flask import current_app as app
from sisdiconpra.persistence import db
from sisdiconpra.models.User import User

name = "sisdiconpra.api.v1.usuarios"
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

@api.route("/", methods=["POST"])
def cria_usuario():
    logger.info("Criando um Usuário")

    teste = User("André", "Lamas3000@gmail.com")
    db.session.add(teste)
    db.session.commit()

    response = Response(
        response=json.dumps({'mensagem': 'Criado um usuário', 'Usuario': teste.json()} ),
        mimetype='application/json',
        status=200
    )
    return response


@api.route("/", methods=["GET"])
def listar_usuarios():
    logger.info("Listando eventos")

    usuarios = User.query.all()

    response = Response(
        response=json.dumps({'mensagem': 'Listando usuários', 'Usuarios': [x.json() for x in usuarios]} ),
        mimetype='application/json',
        status=200
    )
    return response

@api.route("/<id>", methods=["DELETE"])
def apagar_usuario(id):
    logger.info("Apagando um Usuário")

    User.query.filter_by(id=int(id)).delete()
    db.session.commit()

    response = Response(
        response=json.dumps({'mensagem': 'Apagado o usuário id {0}'.format(id)} ),
        mimetype='application/json',
        status=200
    )
    return response