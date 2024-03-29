from models import TRANSAKSI,BARANG,TRANSAKSI_D,KERANJANG
from flask import request
from for_validate import for_validation_transaksi
from flask_jwt_extended import get_jwt_identity
from for_connectionDB import koneksidatabase

def get_all_data_transaksi():
        '''
        get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
        '''
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))
        sort = request.args.get('sort')
        keyword = request.args.get('keyword')
        tipe_sort = request.args.get('tipe_sort')

        return TRANSAKSI.get_all_data_transaksi(
        limit=limit,
        page=page,
        sort = sort,
        tipe_sort= tipe_sort,
        keyword=keyword
    )
def create_transaksi():
    '''
    membuat transaksi dengan memasukkan nama_lengkap, alamat dan user id
    '''
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    TRANSAKSI.create_transaksi(nama_lengkap,alamat,user_id)
    return '',200

def pick_id_transaksi(id):
    '''
    mengambil id transaksi 
    '''
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None :
        return '', 404
    return TRANSAKSI.pick_id_transaksi(id)

def delete_transaksi(id):
    '''
    mengapus transaksi berdasarkan dengan pengecekan id transaksi terlebih dahulu 
    '''
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None:
        return '', 404
    TRANSAKSI.delete_transaksi(id)
    return '',200

def editt_transaksi(id): 
    '''
    mengedit transaksi berdasarkan dengan pengecekan id transaksi terlebih dahulu 
    '''
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
    '''
    melakukan transaksi dan transaksi detail dalam 1 langkah eksekusi 
    memasukkan user id by token dan manual input nama_lengkap,alamat,cart_ids
    dan melakukan transaksi dan melakukan pengulangan dan melakukan transaksi detail 
    '''
    Connection = koneksidatabase.cursor()
    try:
        user_id = get_jwt_identity ()['id']
        nama_lengkap = request.form.get('nama_lengkap')
        alamat = request.form.get('alamat')
        cart_ids = request.form.getlist('id_keranjang')
        for cart_id in cart_ids :
            cart = KERANJANG.coba_pick_id_keranjang(cart_id)
            if cart is None:
                return 'eror data tidak ada di dalam keranjang'
            
            stok_keranjang = int(cart ['kuantitas'])
            produk = BARANG.pick_id_barang(cart['barang_id'])
            test = cart ['barang_id']

            if int(produk['stok']) < (stok_keranjang) :
                return f"stok dari barang dalam keranjang dengan nomor  {produk['id']} tidak mencukupi"
            
            total = cart['harga'] * cart ['kuantitas']

            transaksi = TRANSAKSI.coba_transaksi(nama_lengkap,alamat,user_id)
            TRANSAKSI_D.coba_transaksi(transaksi,test,cart['kuantitas'],total)

            update_kuantitas_barang = produk['stok'] - stok_keranjang
            print(update_kuantitas_barang)
            BARANG.update_kuantitas(update_kuantitas_barang,produk['id'])
        #coba dulu tanpa menghapus keranjang
        koneksidatabase.commit()
        return{'message':'Berhasil ditambahkan'}
    except Exception as e :
        koneksidatabase.rollback()
        raise e
    finally:
        Connection.close() 
        