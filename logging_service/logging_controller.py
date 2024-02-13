from flask import Flask, request

logging = Flask("Logging")

messages = {}

@logging.route('/log', methods=['GET', 'POST'])
def log_web_client():
    try:
        if request.method == 'POST':
            dictionary = request.get_json()
            messages[dictionary['uuid']] = dictionary['msg']
            print(dictionary['msg'])
            return "OK"
        if request.method == 'GET':
            return str(list(messages.values()))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    logging.run(port=8082)