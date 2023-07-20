import json
from flask import request
from pydantic import ValidationError
from dto.customer_dtos.customer_dto import CustomerDto

from dto.customer_dtos.customer_dto import CustomerDto
from errors.errors import CustomerIdNotFoundException, CustomerIdNotFoundException
from service.service import Service
from settings import app, serialize, logger


POST_LIST = '/customers'
PUT_GET_DELETE = '/customers/<customer_id>'


@app.route(POST_LIST, methods=["POST"])
def create_customer():
    try:
        logger.info(request.json)

        customer_dto = CustomerDto(**request.json)

        service = Service()

        customer = service.createCustomer(customer_dto)

        return (json.dumps(customer, default=serialize), 201, {})
    except (ValidationError, ValueError) as e:
        logger.error(e.args[0])
        return ({'Erro de validação': e.args[0]}, 400, {})
    except CustomerIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        logger.error(e.args[0])
        return ({'Erro': e.args[0]}, 500, {})


@app.route(POST_LIST, methods=["GET"])
def get_customers():
    try:
        logger.info(request.query_string)

        limit = request.args.get('limit', 20)

        service = Service()

        customers = service.getCustomers(limit)

        return (json.dumps(customers, default=serialize), 200, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})


@app.route(PUT_GET_DELETE, methods=["GET"])
def get_customer(customer_id):
    try:
        logger.info(request.data)

        service = Service()

        user = service.getCustomer(int(customer_id))

        return (json.dumps(user, default=serialize), 200, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return ({'Erro de validação': value}, 400, {})
    except CustomerIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})


@app.route(PUT_GET_DELETE, methods=["PUT"])
def update_customer(customer_id):
    try:
        logger.info(request.data)

        customer_dto = CustomerDto(**request.json)

        service = Service()

        service.updateCustomer(customer_id, customer_dto)

        return ({}, 204, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return ({'Erro de validação': value}, 400, {})
    except CustomerIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})


@app.route(PUT_GET_DELETE, methods=["DELETE"])
def delete_customer(customer_id):
    try:
        logger.info(request.data)

        service = Service()

        service.deleteCustomer(int(customer_id))

        return ({}, 204, {})
    except (ValidationError, ValueError) as e:
        value = str(e.errors()[0]['msg'])
        return ({'Erro de validação': value}, 400, {})
    except CustomerIdNotFoundException as e:
        return ({'Erro de validação': str(e)}, 400, {})
    except Exception as e:
        return ({'Erro': str(e)}, 500, {})
