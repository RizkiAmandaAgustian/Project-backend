from models import KATEGORI
from flask import request
from for_validate import for_validation_kategori
from flask_jwt_extended import get_jwt_identity

def get_all_data_kategori():
    '''
    get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
    '''
    limit = int(request.args.get("limit", 5))
    page = int(request.args.get("page", 1))
    keyword = request.args.get('keyword')

    return KATEGORI.get_all_data_kategori(
        limit=limit,
        page=page,
        keyword=keyword
    )

def create_kategori():
    '''
    membuat kategori dengan memasukkan label
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None :
        return validated,404
    KATEGORI.create_kategori(label)
    return '',200

def pick_id_kategori(id):
    '''
    mengambil kategori berdasarkan id 
    '''
    get_id = KATEGORI.pick_id_kategori(id)
    if get_id is None :
        return '', 404
    return KATEGORI.pick_id_kategori(id)

def delete_kategori(id):
    '''
    menghapus sebuah kategori dengan mengecek terlebih dahulu sebuah kategori tersebut ada berdasarkan dengan pengecekan id 
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    get_id = KATEGORI.pick_id_kategori(id)
    if get_id is None:
        return '', 404
    KATEGORI.delete_kategori(id)
    return '',200

def editt_kategori(id): 
    '''
    melakukan pengeditan dengan melakukan pengecekan terlebih dahulu dengan pengecekan by id kategori 
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    if KATEGORI.pick_id_kategori(id) is None:
        return '' , 404
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None:
        return validated,404
    KATEGORI.edit_kategori(id,label)
    return '', 200