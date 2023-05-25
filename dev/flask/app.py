from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'received_data': data}), 200
    elif request.method == 'GET':
        return jsonify({'message': 'This is a GET request'}), 200


if __name__ == "__main__":
    app()
