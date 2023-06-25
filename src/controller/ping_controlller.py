import json
from settings import app



@app.route('/ping')
def ping():
    return json.dumps({"msg":"Pong"})