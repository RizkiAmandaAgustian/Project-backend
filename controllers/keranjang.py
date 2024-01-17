from models import KERANJANG
from flask import request
from controllers.for_validate import for_validation_keranjang

def get_all_data_keranjang():
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))

        return KERANJANG.get_all_data_keranjang(
        limit=limit,
        page=page,
    )

def create_keranjang():
    user_id = request.form.get('user_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')

    validated = for_validation_keranjang (user_id,barang_id,kuantitas,)
    if validated is not None :
        return validated,404
    KERANJANG.create_keranjang(user_id,barang_id,kuantitas,)
    return '',200

def pick_id_keranjang(id):
    get_id = KERANJANG.pick_id_keranjang(id)
    if get_id is None :
        return '', 404
    return KERANJANG.pick_id_keranjang(id)

def delete_keranjang(id):
    get_id = KERANJANG.pick_id_keranjang(id)
    if get_id is None:
        return '', 404
    KERANJANG.delete_keranjang(id)
    return '',200

def editt_keranjang(id): 
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