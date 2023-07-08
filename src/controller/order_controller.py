import json
from flask import request
from pydantic import ValidationError

from src.dto.order_dtos.order_dto import OrderDto
from src.errors.errors import OrderIdNotFoundException
from src.service.service import Service
from settings import app, serialize, logger


@app.route('/orders', methods=["POST"])
def create_order():
    try:
        logger.info(request.data)

        order_dto = OrderDto(**request.json)

        service = Service()

        user = service.createOrder(order_dto)

        return (json.dumps(user, default=serialize), 200, {})
    except (ValidationError, ValueError) as e:
        logger.error(e.args[0])
        return ({'Erro de validação': e.args[0]}, 400, {})
    except OrderIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        logger.error(e.args[0])
        return ({'Erro': e.args[0]}, 500, {})


@app.route('/orders', methods=["GET"])
def get_orders():
    try:
        logger.info(request.query_string)

        limit = request.args.get('limit', 20)

        service = Service()

        orders = service.getOrders(limit)

        return (json.dumps(orders), 200, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})


@app.route('/orders/<order_id>', methods=["PUT"])
def update_order(order_id):
    try:
        logger.info(request.data)

        order_dto = OrderDto(**request.json)

        service = Service()

        user = service.updateOrder(order_id, order_dto)

        return (json.dumps(user), 204, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return ({'Erro de validação': value}, 400, {})
    except OrderIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})
