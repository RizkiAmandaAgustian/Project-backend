from models import TRANSAKSI
from flask import request
from controllers.for_validate import for_validation_transaksi

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