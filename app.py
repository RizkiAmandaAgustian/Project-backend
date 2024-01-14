import flask
from controllers import user_login,create_users,ambil_id_users,edit_users,hapus_users,get_all_data_kategori, create_kategori, ambil_id_kategori, hapus_kategori, edit_kategori , get_all_data_barang, create_barang , ambil_id_barang, hapus_barang, edit_barang, get_all_data_keranjang, create_keranjang, ambil_id_keranjang, edit_keranjang, hapus_keranjang, get_all_data_transaksi, create_transaksi, ambil_id_transaksi, edit_transaksi, hapus_transaksi, get_all_data_transaksi_detail, create_transaksi_detail, ambil_id_transaksi_detail, hapus_transaksi_detail, edit_transaksi_detail
from flask import request
from controllers.for_validate import for_validation_kategori,for_validation_barang,for_validation_keranjang,for_validation_transaksi,for_validation_transaksi_detail
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
def login_dulu():
    return user_login()

@app.get('/validate')
@jwt_required()
def validation ():
    users = get_jwt_identity()
    return {'Kamu berhasil login sebagai':users},200

@app.post('/users')
def buat_users():
    return create_users()

@app.get('/users/<int:id>')
def get_id_users(id):
    return ambil_id_users(id)

@app.put('/users/<int:id>')
def put_users(id):
    return edit_users(id)

@app.delete('/users/<int:id>')
def delete_users(id):
    return hapus_users(id)

#KATEGORI

@app.get('/kategori')
def get_all():
    return get_all_data_kategori()

@app.post('/kategori')
def create():
    return create_kategori()

@app.get('/kategori/<int:id>')
def ambil_id(id):
    return ambil_id_kategori(id)

@app.delete('/kategori/<int:id>')
def hapus(id):
    return hapus_kategori (id)

@app.put('/kategori/<int:id>')
def edit(id): 
    return  edit_kategori (id)

#barang

@app.get('/barang')
def get_all_barang():
    return get_all_data_barang ()

@app.post('/barang')
def create_barang():
    return create_barang ()

@app.get('/barang/<int:id>')
def ambil_id_barang(id):
    return ambil_id_barang (id)

@app.delete('/barang/<int:id>')
def hapus_barang(id):
    return hapus_barang (id)

@app.put('/barang/<int:id>')
def edit_barang(id): 
    return edit_barang (id)

#KERANJANG

@app.get('/keranjang')
def get_all_keranjang():
    return get_all_data_keranjang()

@app.post('/keranjang')
def create_keranjang():
    return create_keranjang ()

@app.get('/keranjang/<int:id>')
def ambil_id_keranjang(id):
    return ambil_id_keranjang (id)

@app.delete('/keranjang/<int:id>')
def hapus_keranjang(id):
    return hapus_keranjang (id)

@app.put('/keranjang/<int:id>')
def edit_keranjang(id): 
    return edit_keranjang (id)



# TRANSAKSI

@app.get('/transaksi')
def get_all_transaksi():
    return get_all_data_transaksi()

@app.post('/transaksi')
def create_transaksi():
    return create_transaksi ()

@app.get('/transaksi/<int:id>')
def ambil_id_transaksi(id):
    return ambil_id_transaksi (id)

@app.delete('/transaksi/<int:id>')
def hapus_transaksi(id):
    return hapus_transaksi (id)

@app.put('/transaksi/<int:id>')
def edit_transaksi(id): 
    return edit_transaksi (id)

#transaksi_detail

@app.get('/transaksi_detail')
def get_all_transaksi_detail():
    return get_all_data_transaksi_detail()

@app.post('/transaksi_detail')
def create_transaksi_detail():
    return create_transaksi_detail ()

@app.get('/transaksi_detail/<int:id>')
def ambil_id_transaksi_detail(id):
    return ambil_id_transaksi_detail (id)

@app.delete('/transaksi_detail/<int:id>')
def hapus_transaksi_detail(id):
    return hapus_transaksi_detail (id)

@app.put('/transaksi_detail/<int:id>')
def edit_transaksi_detail(id): 
    return edit_transaksi_detail (id)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)