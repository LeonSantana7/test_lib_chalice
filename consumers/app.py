from chalice import Chalice

app = Chalice(app_name='consumers')

users = {
    "users":[
        {"name": "usuário1", "phone": "47999999999"},
        {"name": "usuário2", "phone": "47999999999"},
        {"name": "usuário3", "phone": "47999999999"},
    ]
}

companies = {
    "companies":[
        {"name": "empresa1", "phone": "47999999999"},
        {"name": "empresa2", "phone": "47999999999"},
        {"name": "empresa3", "phone": "47999999999"},
    ]
}


@app.route('/consumers/person', methods = ['GET'])
def list_person():
    response = {
        "statusCode": 200,
        "body": users
    }
    return response

@app.route('/consumers/person/{id}', methods = ['GET'])
def get_person(id):
    response = {
        "statusCode": 200,
        "body": {id:{"name":"usuário1", "telefone": "47999999999"}}
    }
    return response

@app.route('/consumers/person', methods = ['POST'])
def create_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} criado com sucesso!"
    }
    return response


@app.route('/consumers/person', methods = ['PUT'])
def update_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} atualizado com sucesso!"
    }
    return response


@app.route('/consumers/person', methods = ['DELETE'])
def delete_user():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Usuário {requests_params} deletado com sucesso!"
    }
    return response

##Company

@app.route('/consumers/company/', methods = ['GET'])
def list_companies():
    response = {
        "statusCode": 200,
        "body": companies
    }
    return response

@app.route('/consumers/company/{id}', methods = ['GET'])
def get_companies(id):
    response = {
        "statusCode": 200,
        "body": {id:{"name":"empresa1", "telefone": "47999999999"}}
    }
    return response

@app.route('/consumers/company', methods = ['POST'])
def create_companies():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} criado com sucesso!"
    }
    return response


@app.route('/consumers/company', methods = ['PUT'])
def update_companies():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} atualizado com sucesso!"
    }
    return response


@app.route('/consumers/company', methods = ['DELETE'])
def delete_companies():
    requests_params = app.current_request.json_body
    response = {
        "statusCode": 200,
        "body": f"Empresa {requests_params} deletado com sucesso!"
    }
    return response