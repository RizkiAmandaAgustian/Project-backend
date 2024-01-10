import flask
import for_mechanism
from flask import request
from for_validate import for_validation_kategori,for_validation_barang,for_validation_keranjang
from flask_jwt_extended import(
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity
)
from flask_cors import CORS

app = flask.Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'HALOO'
CORS(app)

#USERS
@app.get('/users')
def login ():
    username = request.form.get('username',None)
    password = request.form.get('password', None)

    if for_mechanism.login(username,password) is None:
        return {'pesan': 'username atau password yang anda masukkan salah'}
    
    accses_token = create_access_token(identity=username)
    return{'anda berhasil login dan berikut akses token anda':accses_token}

@app.get('/validate')
@jwt_required()
def validation ():
    users = get_jwt_identity()
    return {'Kamu berhasil login sebagai':users},200

#KATEGORI

@app.get('/kategori')
def get_all():
    return for_mechanism.get_all_data_kategori()

@app.post('/kategori')
def create():
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None :
        return validated,404
    for_mechanism.create_kategori(label)
    return '',200

@app.get('/kategori/<int:id>')
def ambil_id(id):
    get_id = for_mechanism.pick_id_kategori(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_kategori(id)

@app.delete('/kategori/<int:id>')
def hapus(id):
    get_id = for_mechanism.pick_id_kategori(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_kategori(id)
    return '',200

@app.put('/kategori/<int:id>')
def edit(id): 
    if for_mechanism.pick_id(id) is None:
        return '' , 404
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None:
        return validated,404
    for_mechanism.edit_kategori(id,label)
    return '', 200

#barang

@app.get('/barang')
def get_all_barang():
    return for_mechanism.get_all_data_barang()

@app.post('/barang')
def create_barang():
    nama_barang = request.form.get('nama_barang')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga')
    stok = request.form.get('stok')
    kategori_id = request.form.get('kategori_id')

    validated = for_validation_barang (nama_barang,deskripsi,harga,stok,kategori_id)
    if validated is not None :
        return validated,404
    for_mechanism.create_barang(nama_barang,deskripsi,harga,stok,kategori_id)
    return '',200

@app.get('/barang/<int:id>')
def ambil_id_barang(id):
    get_id = for_mechanism.pick_id_barang(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_barang(id)

@app.delete('/barang/<int:id>')
def hapus_barang(id):
    get_id = for_mechanism.pick_id_barang(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_barang(id)
    return '',200

@app.put('/barang/<int:id>')
def edit_barang(id): 
    if for_mechanism.pick_id_barang(id) is None:
        return '' , 404
    nama_barang = request.form.get('nama_barang')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga')
    stok = request.form.get('stok')
    kategori_id = request.form.get('kategori_id')

    validated = for_validation_barang (nama_barang,deskripsi,harga,stok,kategori_id)
    if validated is not None :
        return validated,404
    for_mechanism.edit_barang(id,nama_barang,deskripsi,harga,stok,kategori_id)
    return '', 200

#KERANJANG

@app.get('/keranjang')
def get_all_keranjang():
    return for_mechanism.get_all_data_keranjang()

@app.post('/keranjang')
def create_keranjang():
    user_id = request.form.get('user_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (user_id,barang_id,kuantitas,)
    if validated is not None :
        return validated,404
    for_mechanism.create_keranjang(user_id,barang_id,kuantitas,)
    return '',200

@app.get('/keranjang/<int:id>')
def ambil_id_keranjang(id):
    get_id = for_mechanism.pick_id_keranjang(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_keranjang(id)

@app.delete('/keranjang/<int:id>')
def hapus_keranjang(id):
    get_id = for_mechanism.pick_id_keranjang(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_keranjang(id)
    return '',200

@app.put('/keranjang/<int:id>')
def edit_keranjang(id): 
    if for_mechanism.pick_id_keranjang(id) is None:
        return '' , 404
    nama_barang = request.form.get('nama_barang')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga')
    stok = request.form.get('stok')
    kategori_id = request.form.get('kategori_id')

    validated = for_validation_keranjang (nama_barang,deskripsi,harga,stok,kategori_id)
    if validated is not None :
        return validated,404
    for_mechanism.edit_keranjang(id,nama_barang,deskripsi,harga,stok,kategori_id)
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)