from flask import Flask, request, jsonify
from validators import validate_feild
from formfinder import find_form

app = Flask(__name__)


@app.route('/get-form', methods=['POST'])
def get_form():
    incoming_fields = {}
    for i, j in request.form.items():
        incoming_fields[i] = validate_feild(str(j).strip())
    payload = find_form(incoming_fields)
    respond = jsonify(payload)
    respond.status_code = 200
    return respond


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8088, debug=True)
