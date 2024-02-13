from flask import Flask, request
import requests
import uuid

facade = Flask("Facade")

logging = "http://localhost:8082/log"
messages = "http://localhost:8081/message"


@facade.route('/facade', methods=['POST', 'GET'])
def facade_web_client_post():
    try:
        if request.method == 'POST':
            id = str(uuid.uuid4())
            msg = request.get_data()
            requests.post(logging, json={'uuid': id, 'msg': msg})
            return "OK"
        if request.method == 'GET':
            response = requests.get(logging)
            message = requests.get(messages)
            return response.text + ':' + message.text, response.status_code, response.headers.items()
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    facade.run(port=8080)
