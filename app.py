import flask
from controllers import  paginasi,user_login,create_users,pick_id_users,editt_users,delete_users,get_all_data_kategori, create_kategori, pick_id_kategori, delete_kategori, editt_kategori , get_all_data_barang, create_barang , pick_id_barang, delete_barang, editt_barang, get_all_data_keranjang, create_keranjang, pick_id_keranjang, editt_keranjang, delete_keranjang, get_all_data_transaksi, create_transaksi, pick_id_transaksi, editt_transaksi, delete_transaksi, get_all_data_transaksi_detail, create_transaksi_detail, pick_id_transaksi_detail, delete_transaksi_detail, editt_transaksi_detail
from flask_jwt_extended import(
    JWTManager,
    jwt_required,
    get_jwt_identity
)
from flask_cors import CORS
import base64

app = flask.Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'HALOO'
CORS(app)

@app.get('/paginasi')
def pagination ():
    return paginasi()

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
    return pick_id_users(id)

@app.put('/users/<int:id>')
def put_users(id):
    return editt_users(id)

@app.delete('/users/<int:id>')
def hapus_users(id):
    return delete_users(id)

#KATEGORI

@app.get('/kategori')
def get_all():
    return get_all_data_kategori()

@app.post('/kategori')
def create():
    return create_kategori()

@app.get('/kategori/<int:id>')
def pick_id(id):
    return pick_id_kategori(id)

@app.delete('/kategori/<int:id>')
def hapus(id):
    return delete_kategori (id)

@app.put('/kategori/<int:id>')
def edit(id): 
    return  editt_kategori (id)

#barang

@app.get('/barang')
def get_all_barang():
    return get_all_data_barang ()

@app.post('/barang')
def buat_barang():
    return create_barang()

@app.get('/barang/<int:id>')
def pick_id_barang(id):
    return pick_id_barang (id)

@app.delete('/barang/<int:id>')
def hapus_barang(id):
    return delete_barang (id)

@app.put('/barang/<int:id>')
def edit_barangg(id): 
    return editt_barang (id)

#KERANJANG

@app.get('/keranjang')
def get_all_keranjang():
    return get_all_data_keranjang()

@app.post('/keranjang')
def create_keranjang():
    return create_keranjang ()

@app.get('/keranjang/<int:id>')
def pick_id_keranjang(id):
    return pick_id_keranjang (id)

@app.delete('/keranjang/<int:id>')
def hapus_keranjang(id):
    return delete_keranjang (id)

@app.put('/keranjang/<int:id>')
def edit_keranjang(id): 
    return editt_keranjang (id)



# TRANSAKSI

@app.get('/transaksi')
def get_all_transaksi():
    return get_all_data_transaksi()

@app.post('/transaksi')
def create_transaksi():
    return create_transaksi ()

@app.get('/transaksi/<int:id>')
def pick_id_transaksi(id):
    return pick_id_transaksi (id)

@app.delete('/transaksi/<int:id>')
def hapus_transaksi(id):
    return delete_transaksi (id)

@app.put('/transaksi/<int:id>')
def edit_transaksi(id): 
    return editt_transaksi (id)

#transaksi_detail

@app.get('/transaksi_detail')
def get_all_transaksi_detail():
    return get_all_data_transaksi_detail()

@app.post('/transaksi_detail')
def create_transaksi_detail():
    return create_transaksi_detail ()

@app.get('/transaksi_detail/<int:id>')
def pick_id_transaksi_detail(id):
    return pick_id_transaksi_detail (id)

@app.delete('/transaksi_detail/<int:id>')
def hapus_transaksi_detail(id):
    return delete_transaksi_detail (id)

@app.put('/transaksi_detail/<int:id>')
def edit_transaksi_detail(id): 
    return editt_transaksi_detail (id)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)