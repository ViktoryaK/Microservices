from flask import Flask, request
import hazelcast

logging = Flask("Logging")

client1 = hazelcast.HazelcastClient(
    cluster_name="hw3",
    cluster_members=["172.18.0.2:5701"]
    # cluster_members=["172.18.0.4:5701"]
    # cluster_members=["172.18.0.5:5701"]
)

@logging.route('/log', methods=['GET', 'POST'])
def log_web_client():
    messages = client1.get_map("distributed-map").blocking()
    try:
        if request.method == 'POST':
            dictionary = request.get_json()
            messages.put(dictionary['uuid'], dictionary['msg'])
            print(dictionary['msg'])
            return "OK"
        if request.method == 'GET':
            return str(list(messages.values()))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    logging.run(port=8082)
    # logging.run(port=8083)
    # logging.run(port=8084)
    client1.shutdown()
