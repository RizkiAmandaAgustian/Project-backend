from flask import request
from flask_jwt_extended import create_access_token
from controllers.for_validate import for_validation_kategori,for_validation_barang,for_validation_keranjang,for_validation_transaksi,for_validation_transaksi_detail,for_validation_users
from models import for_mechanism

def user_login ():
    username = request.form.get('username', None)
    password = request.form.get('password', None)

    login_user = for_mechanism.login_users(username,password)
    if login_user:
        accses_token = create_access_token(identity=username)
        return{'LOGIN BERHASIL DAN TOKEN ANDA': accses_token}
    return{'USERNAME ATAU PASSWORD SALAH'},404

def create_users():
    username = request.form.get('username')
    password = request.form.get('password')
    nama_lengkap = request.form.get('nama_lengkap')
    validated = for_validation_users (username,password,nama_lengkap)
    if validated is not None :
        return validated,404
    for_mechanism.create_users(username,password,nama_lengkap)
    return '',200

def ambil_id_users(id):
    get_id = for_mechanism.pick_id_users(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_users(id)

def hapus_users(id):
    get_id = for_mechanism.pick_id_users(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_users(id)
    return '',200

def edit_users(id): 
    if for_mechanism.pick_id_users(id) is None:
        return '' , 404
    username = request.form.get('username')
    password = request.form.get('password')
    nama_lengkap = request.form.get('nama_lengkap')
    validated = for_validation_users (username,password, nama_lengkap)
    if validated is not None:
        return validated,404
    for_mechanism.edit_users(id,username,password, nama_lengkap)
    return '', 200

#kategori

def get_all_data_kategori():
    items = for_mechanism.get_all_data_kategori()
    if request.args.get('keyword') is not None:
        keyword = request.args.get('keyword')

        _items = []
        for item in items:
            if keyword in item['label'].lower():
                _items.append(item)
        items = _items

    return items
def create_kategori():
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None :
        return validated,404
    for_mechanism.create_kategori(label)
    return '',200

def ambil_id_kategori(id):
    get_id = for_mechanism.pick_id_kategori(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_kategori(id)

def hapus_kategori(id):
    get_id = for_mechanism.pick_id_kategori(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_kategori(id)
    return '',200

def edit_kategori(id): 
    if for_mechanism.pick_id(id) is None:
        return '' , 404
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None:
        return validated,404
    for_mechanism.edit_kategori(id,label)
    return '', 200

#Barang

def get_all_data_barang():
    items = for_mechanism.get_all_data_barang()
    if request.args.get('keyword') is not None:
        keyword = request.args.get('keyword')

        _items = []
        for item in items:
            if keyword in item['label'].lower():
                _items.append(item)
        items = _items
    return items

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

def ambil_id_barang(id):
    get_id = for_mechanism.pick_id_barang(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_barang(id)

def hapus_barang(id):
    get_id = for_mechanism.pick_id_barang(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_barang(id)
    return '',200

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

def get_all_data_keranjang():
    items = for_mechanism.get_all_data_keranjang()
    if request.args.get('keyword') is not None:
        keyword = request.args.get('keyword')

        _items = []
        for item in items:
            if keyword in item['label'].lower():
                _items.append(item)
        items = _items
    return items

def create_keranjang():
    user_id = request.form.get('user_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (user_id,barang_id,kuantitas,)
    if validated is not None :
        return validated,404
    for_mechanism.create_keranjang(user_id,barang_id,kuantitas,)
    return '',200

def ambil_id_keranjang(id):
    get_id = for_mechanism.pick_id_keranjang(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_keranjang(id)

def hapus_keranjang(id):
    get_id = for_mechanism.pick_id_keranjang(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_keranjang(id)
    return '',200

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

#TRANSAKSI 

def get_all_data_transaksi():
    items = for_mechanism.get_all_data_transaksi()
    if request.args.get('keyword') is not None:
        keyword = request.args.get('keyword')

        _items = []
        for item in items:
            if keyword in item['label'].lower():
                _items.append(item)
        items = _items
    return items

def create_transaksi():
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    for_mechanism.create_transaksi(nama_lengkap,alamat,user_id)
    return '',200

def ambil_id_transaksi(id):
    get_id = for_mechanism.pick_id_transaksi(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_transaksi(id)

def hapus_transaksi(id):
    get_id = for_mechanism.pick_id_transaksi(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_transaksi(id)
    return '',200

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

#TRANSAKSI DETAIL

def get_all_data_transaksi_detail():
    items = for_mechanism.get_all_data_transaksi_detail()
    if request.args.get('keyword') is not None:
        keyword = request.args.get('keyword')

        _items = []
        for item in items:
            if keyword in item['label'].lower():
                _items.append(item)
        items = _items
    return items

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
    
def ambil_id_transaksi_detail(id):
    get_id = for_mechanism.pick_id_transaksi_detail(id)
    if get_id is None :
        return '', 404
    return for_mechanism.pick_id_transaksi_detail(id)
    
def hapus_transaksi_detail(id):
    get_id = for_mechanism.pick_id_transaksi_detail(id)
    if get_id is None:
        return '', 404
    for_mechanism.delete_transaksi_detail(id)
    return '',200
    
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

