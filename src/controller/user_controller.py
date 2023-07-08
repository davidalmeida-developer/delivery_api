import json
from flask import request
from pydantic import ValidationError
from src.errors.errors import UserAlreadyExistsException

from src.dto.user_dtos.login_dto import LoginDto
from src.dto.user_dtos.user_dto import UserDto
from src.service.service import Service
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
        print(request.data)

        register_data = UserDto(**request.json)

        service = Service()

        user = service.register(user_dto=register_data)

        return (json.dumps(user), 201, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return ({'Erro de validação': value}, 400, {})
    except (UserAlreadyExistsException) as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})
