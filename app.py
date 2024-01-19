import flask
from controllers import barang,keranjang,transaksi,transaksi_d,kategori,user,sql,gambar
from flask_jwt_extended import(
    JWTManager,
    jwt_required,
    get_jwt_identity
)
from flask_cors import CORS

app = flask.Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'HALOO'
CORS(app)

# @app.get('/paginasi')
# def pagination ():
#     return kontrol.paginasi()

#USERS
@app.get('/users')
def login_dulu():
    return user.user_login ()

@app.get('/validate')
@jwt_required()
def validation ():
    users = get_jwt_identity()
    return{'Kamu berhasil login sebagai':users},200

@app.post('/users')
def buat_users():
    return user.create_users()

@app.get('/users/<int:id>')
def get_id_users(id):
    return user.pick_id_users(id)

@app.put('/users/<int:id>')
def put_users(id):
    return user.editt_users(id)

@app.delete('/users/<int:id>')
def hapus_users(id):
    return user.delete_users(id)

#KATEGORI

@app.get('/kategori')
def get_all():
    return barang.get_all_data_barang()

@app.post('/kategori')
def create():
    return kategori.create_kategori()

@app.get('/kategori/<int:id>')
def pick_id(id):
    return kategori.pick_id_kategori(id)

@app.delete('/kategori/<int:id>')
def hapus(id):
    return kategori.delete_kategori (id)

@app.put('/kategori/<int:id>')
def edit(id): 
    return kategori.editt_kategori (id)

#barang

@app.get('/barang')
def dapatkan_all_barang():
    return barang.get_all_data_barang()

@app.post('/barang')
def buat_barang():
    return barang.create_barang()

@app.get('/barang/<int:id>')
def pick_id_barang(id):
    return barang.pick_id_barang (id)

@app.delete('/barang/<int:id>')
def hapus_barang(id):
    return barang.delete_barang (id)

@app.put('/barang/<int:id>')
def edit_barangg(id): 
    return barang.edit_barang (id)

#KERANJANG

@app.get('/keranjang')
def get_all_keranjang():
    return keranjang.get_all_data_keranjang()

@app.post('/keranjang')
def buat_keranjang():
    return keranjang.create_keranjang ()

@app.get('/keranjang/<int:id>')
def ambil_id_keranjang(id):
    return keranjang.pick_id_keranjang (id)

@app.delete('/keranjang/<int:id>')
def hapus_keranjang(id):
    return keranjang.delete_keranjang (id)

@app.put('/keranjang/<int:id>')
def edit_keranjang(id): 
    return keranjang.editt_keranjang (id)



# TRANSAKSI

@app.get('/transaksi')
def ambil_all_transaksi():
    return transaksi.get_all_data_transaksi()

@app.post('/transaksi')
def buat_transaksi():
    return transaksi.create_transaksi ()

@app.get('/transaksi/<int:id>')
def ambil_id_transaksi(id):
    return transaksi.pick_id_transaksi (id)

@app.delete('/transaksi/<int:id>')
def hapus_transaksi(id):
    return transaksi.delete_transaksi (id)

@app.put('/transaksi/<int:id>')
def edit_transaksi(id): 
    return transaksi.editt_transaksi (id)

#transaksi_detail

@app.get('/transaksi_detail')
def ambil_all_transaksi_detail():
    return transaksi_d.get_all_data_transaksi_detail()

@app.post('/transaksi_detail')
def buat_transaksi_detail():
    return transaksi_d.create_transaksi_detail ()

@app.get('/transaksi_detail/<int:id>')
def  ambil_id_transaksi_detail(id):
    return transaksi_d.pick_id_transaksi_detail (id)

@app.delete('/transaksi_detail/<int:id>')
def hapus_transaksi_detail(id):
    return transaksi_d.delete_transaksi_detail (id)

@app.put('/transaksi_detail/<int:id>')
def edit_transaksi_detail(id): 
    return transaksi_d.editt_transaksi_detail (id)

#UPLOAD
@app.post('/upload')
def unggah():
    return gambar.upload_gambar()

@app.post('/uploads/<int:id>')
def edit_gambar(id):
    return gambar.edit_gambar(id)

@app.get('/gambar/<int:id>')
def ambil_id_gambar(id):
    return gambar.get_id_gambar(id)

@app.delete('/gambar/<int:id>')
def hapus_gambar(id):
    return gambar.hapus_gambar(id)

@app.get('/SQLJOIN')
def JOIN():
    return sql.sqlQ()

@app.get('/cobasqlsendiri')
def tes ():
    return sql.sqllljoin() #berhasil

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5002, use_reloader = True)