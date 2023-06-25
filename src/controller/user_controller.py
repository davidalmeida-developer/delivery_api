import json

from flask import request, jsonify
from pydantic import ValidationError

from src.dto.login_dto import LoginDto
from src.dto.user_dto import UserDto
from src.service.service import Service
from settings import app, serialize



@app.route('/login',methods=["POST"])
def login():
    try:    
        login_data = LoginDto(**request.json) 

        service = Service()

        user = service.login(login_data=login_data)

        return (json.dumps(user, default=serialize), 200, {})
    except (ValidationError, ValueError) as e:
        return({'Erro de validação': e.args[0]}, 400, {})
    
    except Exception as e:
        return ({'Erro': e.args[0]}, 500, {})


@app.route('/register',methods=["POST"])
def register():
    try:    
        register_data = UserDto(**request.json)

        service = Service()

        user = service.register(user_data=register_data)

        return (json.dumps(user), 200, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return({'Erro de validação': value}, 400, {})
    except Exception as e:
        return ({'Erro': e}, 500, {})
    
