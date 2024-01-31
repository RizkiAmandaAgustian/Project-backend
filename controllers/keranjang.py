from models import KERANJANG
from flask import request
from for_validate import for_validation_keranjang
from flask_jwt_extended import get_jwt_identity

def get_all_data_keranjang():
        '''
        get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
        '''
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))

        return KERANJANG.get_all_data_keranjang(
        limit=limit,
        page=page,
    )

def create_keranjang():
    '''
    membuat keranjang dengan user id otomatis karena mengambil id dari token dan tinggal memasukkan id barang dan kuantitas 
    '''
    user_id = get_jwt_identity()["id"] #membuat kita bisa memasukkan langsung id ke bagian keranjang
    print(user_id)
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (barang_id,kuantitas)
    if validated is not None :
        return validated,404
    KERANJANG.create_keranjang(user_id,barang_id,kuantitas)
    print(user_id)
    return '',200

def pick_id_keranjang(id):
    '''
    mengambil id keranjang 
    '''
    get_id = KERANJANG.pick_id_keranjang(id)
    if get_id is None :
        return '', 404
    return KERANJANG.pick_id_keranjang(id)

def delete_keranjang(id):
    '''
    menghapus keranjang dengan memasukkan id dari keranjang dan id tersebut tersedia 
    '''
    get_id = KERANJANG.pick_id_keranjang(id)
    if get_id is None:
        return '', 404
    KERANJANG.delete_keranjang(id)
    return '',200

def editt_keranjang(id): 
    '''
    mengedit keranjang dengan memasukkan id dari keranjang dan id tersebut tersedia 
    '''
    if KERANJANG.pick_id_keranjang(id) is None:
        return '' , 404
    user_id = request.form.get('user_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (user_id,barang_id,kuantitas)
    if validated is not None :
        return validated,404
    KERANJANG.edit_keranjang(id,user_id,barang_id,kuantitas)
    return '', 200