import random
import hazelcast
from flask import Flask, request
import requests
import uuid

facade = Flask("Facade")

logging = ["http://localhost:8082/log", "http://localhost:8083/log", "http://localhost:8084/log"]
messages = ["http://localhost:8081/message", "http://localhost:8086/message"]

client = hazelcast.HazelcastClient(
        cluster_name="hw3",
        cluster_members=["172.18.0.6:5701"]
    )
queue = client.get_queue("messages-queue").blocking()
@facade.route('/facade', methods=['POST', 'GET'])
def facade_web_client_post():
    try:
        if request.method == 'POST':
            id = str(uuid.uuid4())
            msg = request.get_data()
            requests.post(random.choice(logging), json={'uuid': id, 'msg': msg})
            queue.put(msg)
            return "OK"
        if request.method == 'GET':
            response = requests.get(random.choice(logging))
            message = requests.get(random.choice(messages))
            return response.text + ':' + message.text, response.status_code, response.headers.items()
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    facade.run(port=8085)
    client.shutdown()
