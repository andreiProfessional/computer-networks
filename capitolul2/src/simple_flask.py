from flask import Flask, jsonify
from flask import request
import socket
import math

app = Flask(__name__)

@app.route('/')
def hello():
    nume = "Nicula Andrei Alexandru"
    numar_matricol = "312/2024"
    return "Nume: " + nume + "<br>" + "Numar matricol: " + numar_matricol + "<br>"

@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})

@app.route('/ip', methods=['GET'])
def get_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return jsonify({"ip": ip})

@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):
    return jsonify({"item_id": item_id})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/subnet', methods=['GET'])
def subnet_mask():
    numar_noduri = int(request.args.get("noduri", 0))
    biti_host = math.ceil(math.log2(numar_noduri + 2))
    prefix = 32 - biti_host
    biti = []
    for _ in range(prefix):
        biti.append(1)
    for _ in range(biti_host):
        biti.append(0)
    octeti = []
    for i in range(4):
        octet = 0
        for j in range(8):
            octet = octet * 2 + biti[8 * i + j]
        octeti.append(octet)
    subnet_mask = ".".join(map(str, octeti))
    return jsonify({"subnet_mask": subnet_mask, "prefix": f"/{prefix}"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
