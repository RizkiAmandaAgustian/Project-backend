import flask
import for_mechanism
from flask import request
from for_validate import for_validation_kategori,for_validation_barang,for_validation_keranjang,for_validation_transaksi,for_validation_transaksi_detail
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
    user_id = request.form.get('user_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (user_id,barang_id,kuantitas)
    if validated is not None :
        return validated,404
    for_mechanism.edit_keranjang(id,user_id,barang_id,kuantitas)
    return '', 200



# TRANSAKSI

@app.get('/transaksi')
def get_all_transaksi():
    return for_mechanism.get_all_data_transaksi()

@app.post('/transaksi')
def create_transaksi():
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    for_mechanism.create_transaksi(nama_lengkap,alamat,user_id)
    return '',200

@app.get('/transaksi/<int:id>')
def ambil_id_transaksi(id):
    get_id = for_mechanism.pick_id_transaksi(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_transaksi(id)

@app.delete('/transaksi/<int:id>')
def hapus_transaksi(id):
    get_id = for_mechanism.pick_id_transaksi(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_transaksi(id)
    return '',200

@app.put('/transaksi/<int:id>')
def edit_transaksi(id): 
    if for_mechanism.pick_id_transaksi(id) is None:
        return '' , 404
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    for_mechanism.edit_transaksi(id,nama_lengkap,alamat,user_id)
    return '', 200

#transaksi_detail

@app.get('/transaksi_detail')
def get_all_transaksi_detail():
    return for_mechanism.get_all_data_transaksi_detail()

@app.post('/transaksi_detail')
def create_transaksi_detail():
    transaksi_id = request.form.get('transaksi_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')
    harga = request.form.get('harga')

    validated = for_validation_transaksi_detail (transaksi_id,barang_id,kuantitas,harga)
    if validated is not None :
        return validated,404
    for_mechanism.create_transaksi_detail(transaksi_id,barang_id,kuantitas,harga)
    return '',200

@app.get('/transaksi_detail/<int:id>')
def ambil_id_transaksi_detail(id):
    get_id = for_mechanism.pick_id_transaksi_detail(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_transaksi_detail(id)

@app.delete('/transaksi_detail/<int:id>')
def hapus_transaksi_detail(id):
    get_id = for_mechanism.pick_id_transaksi_detail(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_transaksi_detail(id)
    return '',200

@app.put('/transaksi_detail/<int:id>')
def edit_transaksi_detail(id): 
    if for_mechanism.pick_id_transaksi_detail(id) is None:
        return '' , 404
    transaksi_id = request.form.get('transaksi_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')
    harga = request.form.get('harga')

    validated = for_validation_transaksi_detail (transaksi_id,barang_id,kuantitas,harga)
    if validated is not None :
        return validated,404
    for_mechanism.edit_transaksi_detail(id,transaksi_id,barang_id,kuantitas,harga)
    return '', 200


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)