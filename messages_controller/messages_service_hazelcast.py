from flask import Flask, request
import hazelcast
from threading import Thread

messages = Flask("Messages")

client1 = hazelcast.HazelcastClient(
    cluster_name="hw3",
    cluster_members=["172.18.0.6:5701"]
)

queue = client1.get_queue("messages-queue").blocking()
msgs = []


def post():
    while True:
        item = queue.take().decode("utf-8")
        print(item)
        msgs.append(item)

Thread(target=post, daemon=True).start()


@messages.route('/message', methods=['GET'])
def message_web_client():
    try:
        if request.method == 'GET':
            return msgs
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    # messages.run(port=8081)
    messages.run(port=8086)
    client1.shutdown()
    queue.clear()
