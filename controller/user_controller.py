import json
from flask import request
from pydantic import ValidationError
from errors.errors import UserAlreadyExistsException

from dto.user_dtos.login_dto import LoginDto
from dto.user_dtos.user_dto import UserDto
from service.service import Service
from settings import app, serialize, logger


@app.route('/login', methods=["POST"])
def login():
    try:
        logger.info(request.data)

        login_dto = LoginDto(**request.json)

        service = Service()

        user = service.login(login_dto)

        return (json.dumps(user, default=serialize), 200, {})
    except (ValidationError, ValueError) as e:
        return ({'Erro de validação': e.args[0]}, 400, {})

    except Exception as e:
        return ({'Erro': e.args[0]}, 500, {})


@app.route('/register', methods=["POST"])
def register():
    try:
        logger.info(request.json)

        user_dto = UserDto(**request.json)

        service = Service()

        user = service.register(user_dto=user_dto)

        return (json.dumps(user), 201, {})
    except (ValidationError, ValueError) as e:
        value = f'{str(e.errors()[0]["msg"])}: {str(e.errors()[0]["loc"][0])}'
        return ({'Erro de validação': value}, 400, {})
    except (UserAlreadyExistsException) as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})
