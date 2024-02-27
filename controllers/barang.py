from models import BARANG
from flask import request
from for_validate import for_validation_barang
from flask_jwt_extended import get_jwt_identity

def get_all_data_barang():
    '''
    get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
    '''
    keyword = request.args.get('keyword')
    limit = int(request.args.get("limit", 3))
    page = int(request.args.get("page", 1))
    sort = request.args.get('sort')
    tipe_data_sort = request.args.get('tipe_data_sort')
    items = BARANG.get_all_data_barang(
        limit=limit,
        page=page,
        keyword=keyword,
        sort=sort,
        tipe_data_sort=tipe_data_sort
    )
    

    return items
    


def create_barang():
    '''
    create_barang untuk menambahkan barang ke database dengan mengisi nama_barang,deskripsi,harga,stok,kategori_id
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    nama_barang = request.form.get('nama_barang')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga')
    stok = request.form.get('stok')
    kategori_id = request.form.get('kategori_id')

    validated = for_validation_barang (nama_barang,deskripsi,harga,stok,kategori_id)
    if validated is not None :
        return validated,404
    BARANG.create_barang(nama_barang,deskripsi,harga,stok,kategori_id)
    return '',200

def pick_id_barang(id):
    '''
    mendapatkan barang berdasarkan id nya
    '''
    get_id = BARANG.pick_id_barang(id)
    if get_id is None :
        return '', 404      
    return BARANG.pick_id_barang(id)

def delete_barang(id):
    '''
    menghapus barang namun memasukkan id terlebih dahulu untuk melihat apakah id barang tersebut ada 
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    get_id = BARANG.pick_id_barang(id)
    if get_id is None:
        return '', 404
    BARANG.delete_barang(id)
    return '',200

def editt_barang(id): 
    '''
    melakukan edit barang dengan mengecek id terlebih dahulu sebelum mengedit data dalam barang
    
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    if BARANG.pick_id_barang(id) is None:
        return '' , 404
    nama_barang = request.form.get('nama_barang')
    deskripsi = request.form.get('deskripsi')
    harga = request.form.get('harga')
    stok = request.form.get('stok')
    kategori_id = request.form.get('kategori_id')

    validated = for_validation_barang (nama_barang,deskripsi,harga,stok,kategori_id)
    if validated is not None :
        return validated,404
    BARANG.edit_barang(id,nama_barang,deskripsi,harga,stok,kategori_id)
    return '', 200

def update_stok(id):
    stok = request.form.get('stok')
    BARANG.update_stok(stok,id)
    return '', 200
