from models import TRANSAKSI,BARANG,TRANSAKSI_D,KERANJANG
from flask import request
from for_validate import for_validation_transaksi
from flask_jwt_extended import get_jwt_identity
from static.for_connectionDB import koneksidatabase

def get_all_data_transaksi():
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))

        return TRANSAKSI.get_all_data_transaksi(
        limit=limit,
        page=page,
    )
def create_transaksi():
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    TRANSAKSI.create_transaksi(nama_lengkap,alamat,user_id)
    return '',200

def pick_id_transaksi(id):
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None :
        return '', 404
    return TRANSAKSI.pick_id_transaksi(id)

def delete_transaksi(id):
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None:
        return '', 404
    TRANSAKSI.delete_transaksi(id)
    return '',200

def editt_transaksi(id): 
    if TRANSAKSI.pick_id_transaksi(id) is None:
        return '' , 404
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    TRANSAKSI.edit_transaksi(id,nama_lengkap,alamat,user_id)
    return '', 200

def coba_transaksi():
    Connection = koneksidatabase.cursor()
    try:
        user_id = get_jwt_identity ()['id']
        nama_lengkap = request.form.get('nama_lengkap')
        alamat = request.form.get('alamat')
        cart_ids = request.form.getlist('id_keranjang')
        transaksi = TRANSAKSI.coba_transaksi(user_id,alamat,nama_lengkap)
        for cart_id in cart_ids :
            cart = KERANJANG.pick_id_keranjang(cart_id,user_id)
            if cart is None:
                return 'eror data tidak ada di database'
            produk = BARANG.pick_id_barang(cart['id'])
            total = cart['barang_id'] * cart ['kuantitas']
            TRANSAKSI_D.coba_transaksi(transaksi['id'],produk['id'],cart['kuantitas'],cart ['barang_id'],total)
        #coba dulu tanpa menghapus keranjang
        koneksidatabase.commit()
        return{'message':'Berhasil ditambahkan'}
    except Exception as e :
        koneksidatabase.rollback()
        raise e
    finally:
        Connection.close() 
        