from flask import Flask, jsonify
from flask import request
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    nume = "Nicula Andrei Alexandru"
    numar_matricol = "312/2024"
    return "Nume: " + nume + "<br>" + "Numar matricol: " + numar_matricol + "<br>"

'''
This method expects a json content.
Use header: 'Content-Type: application/json'
'''
@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})

@app.route('/ip')
def get_ip():
    host_name_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({"ip": host_name_ip})
    


@app.route('/item/<item_id>')
def get_item(item_id):
    return jsonify({"item_id": item_id})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
