import flask
import for_mechanism
from flask import request
from for_validate import validation

app = flask.Flask(__name__)

@app.get('/laptop')
def get_all():
    return for_mechanism.get_all_data()

@app.post('/laptop')
def create():
    seri_laptop = request.form.get('seri_laptop')
    support_thunderbolt = request.form.get('support_thunderbolt')
    validated = validation (seri_laptop,support_thunderbolt)
    if validated is not None :
        return validated,404
    support_thunderbolt = bool(int(support_thunderbolt))
    for_mechanism.create(seri_laptop,support_thunderbolt)
    return '',200

@app.get('/laptop/<int:no>')
def ambil_id(no):
    get_id = for_mechanism.pick_id(no)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id(no)    


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)