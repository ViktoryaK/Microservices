from flask import Flask

messages = Flask("Messages")

@messages.route('/message', methods=['GET'])
def message_web_client():
    try:
        return "Message-service not implemented yet \n"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    messages.run(port=8081)