from dotenv import load_dotenv
load_dotenv ()
import flask
from controllers import barang,keranjang,transaksi,transaksi_d,kategori,user,sql,gambar
from flask_bcrypt import Bcrypt
from flask_jwt_extended import(
    JWTManager,
    jwt_required,
    get_jwt_identity
)
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'HALOO'
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

# @app.get('/paginasi')
# def pagination ():
#     return kontrol.paginasi()

#USERS
@app.post('/users/login')
def login_dulu():
    return user.user_login ()

@app.get('/validate_login')
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

@app.put('/users')
@jwt_required()
def put_current_users():
    id=get_jwt_identity()['id']
    return user.editt_users(id)


@app.delete('/users')
@jwt_required()
def hapus_users():
    id=get_jwt_identity()['id']
    return user.delete_users(id)

#KATEGORI

@app.get('/kategori')
@jwt_required()
def get_all():
    return kategori.get_all_data_kategori()

@app.post('/kategori')
@jwt_required()
def create():
    return kategori.create_kategori()

@app.get('/kategori/<int:id>')
@jwt_required()
def pick_id(id):
    return kategori.pick_id_kategori(id)

@app.delete('/kategori/<int:id>')
@jwt_required()
def hapus(id):
    return kategori.delete_kategori (id)

@app.put('/kategori/<int:id>')
@jwt_required()
def edit(id): 
    return kategori.editt_kategori (id)

#barang

@app.get('/barang')
@jwt_required()
def dapatkan_all_barang():
    return barang.get_all_data_barang()

@app.post('/barang')
@jwt_required()
def buat_barang():
    return barang.create_barang()

@app.get('/barang/<int:id>')
@jwt_required()
def pick_id_barang(id):
    return barang.pick_id_barang (id)

@app.delete('/barang/<int:id>')
@jwt_required()
def hapus_barang(id):
    return barang.delete_barang (id)

@app.put('/barang/<int:id>')
@jwt_required()
def edit_barangg(id): 
    return barang.editt_barang (id)

@app.post('/barang/<int:id>/stok')
@jwt_required()
def stok (id):
    return barang.update_stok(id)

#KERANJANG

@app.get('/keranjang')
@jwt_required()
def get_all_keranjang():
    return keranjang.get_all_data_keranjang()

@app.post('/keranjang')
@jwt_required()
def buat_keranjang():
    return keranjang.create_keranjang ()

@app.get('/keranjang/<int:id>')
@jwt_required()
def ambil_id_keranjang(id):
    return keranjang.pick_id_keranjang (id)

@app.delete('/keranjang/<int:id>')
@jwt_required()
def hapus_keranjang(id):
    return keranjang.delete_keranjang (id)

@app.put('/keranjang/<int:id>')
@jwt_required()
def edit_keranjang(id): 
    return keranjang.editt_keranjang (id)



# TRANSAKSI

@app.get('/transaksi')
@jwt_required()
def ambil_all_transaksi():
    return transaksi.get_all_data_transaksi()

@app.post('/transaksi')
@jwt_required()
def cobaaja():
    return transaksi.coba_transaksi()

@app.get('/transaksi/<int:id>')
@jwt_required()
def ambil_id_transaksi(id):
    return transaksi.pick_id_transaksi (id)

@app.delete('/transaksi/<int:id>')
@jwt_required()
def hapus_transaksi(id):
    return transaksi.delete_transaksi (id)

@app.put('/transaksi/<int:id>')
@jwt_required()
def edit_transaksi(id): 
    return transaksi.editt_transaksi (id)

#transaksi_detail

@app.get('/transaksi_detail')
@jwt_required()
def ambil_all_transaksi_detail():
    return transaksi_d.get_all_data_transaksi_detail()

@app.post('/transaksi_detail')
@jwt_required()
def buat_transaksi_detail():
    return transaksi_d.create_transaksi_detail ()

@app.get('/transaksi_detail/<int:id>')
@jwt_required()
def  ambil_id_transaksi_detail(id):
    return transaksi_d.pick_id_transaksi_detail (id)

@app.delete('/transaksi_detail/<int:id>')
@jwt_required()
def hapus_transaksi_detail(id):
    return transaksi_d.delete_transaksi_detail (id)

@app.put('/transaksi_detail/<int:id>')
@jwt_required()
def edit_transaksi_detail(id): 
    return transaksi_d.editt_transaksi_detail (id)

#UPLOAD
@app.post('/upload')
@jwt_required()
def unggah():
    return gambar.upload_gambar()

@app.post('/gambar/<int:id>')
@jwt_required()
def edit_gambar(id):
    return gambar.edit_gambar(id)

@app.get('/gambar/<int:id>')
@jwt_required()
def ambil_id_gambar(id):
    return gambar.get_id_gambar(id)

@app.delete('/gambar/<int:id>')
@jwt_required()
def hapus_gambar(id):
    return gambar.hapus_gambar(id)

@app.get('/SQLJOIN')
def JOIN():
    return sql.sqlQ()

@app.get('/cobasqlsendiri')
def tes ():
    return sql.sqllljoin() #berhasil


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002, use_reloader = True)