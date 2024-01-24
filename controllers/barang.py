from models import BARANG
from flask import request
from for_validate import for_validation_barang

def get_all_data_barang():
    keyword = request.args.get('keyword')
    limit = int(request.args.get("limit", 3))
    page = int(request.args.get("page", 1))

    items = BARANG.get_all_data_barang(
        limit=limit,
        page=page,
        keyword=keyword
    )
    

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
    BARANG.create_barang(nama_barang,deskripsi,harga,stok,kategori_id)
    return '',200

def pick_id_barang(id):
    get_id = BARANG.pick_id_barang(id)
    if get_id is None :
        return '', 404      
    return BARANG.pick_id_barang(id)

def delete_barang(id):
    get_id = BARANG.pick_id_barang(id)
    if get_id is None:
        return '', 404
    BARANG.delete_barang(id)
    return '',200

def editt_barang(id): 
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
