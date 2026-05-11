from flask import Flask, jsonify, request

app = Flask(__name__)
accounts = []
next_id = 1

@app.route('/accounts', methods=['POST'])
def create_account():
    global next_id
    data = request.get_json()
    account = {'id': next_id, 'name': data['name'], 'email': data['email']}
    accounts.append(account)
    next_id += 1
    return jsonify(account), 201

@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts)

@app.route('/accounts/<int:id>', methods=['GET'])
def read_account(id):
    account = next((a for a in accounts if a['id'] == id), None)
    return jsonify(account) if account else ('', 404)

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    data = request.get_json()
    for a in accounts:
        if a['id'] == id:
            a.update(data)
            return jsonify(a)
    return ('', 404)

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    global accounts
    accounts = [a for a in accounts if a['id'] != id]
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
