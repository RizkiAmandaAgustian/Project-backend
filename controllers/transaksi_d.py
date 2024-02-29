from models import TRANSAKSI_D
from flask import request
from for_validate import for_validation_transaksi_detail

def get_all_data_transaksi_detail():
    '''
    get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
    '''
    limit = int(request.args.get("limit", 5))
    page = int(request.args.get("page", 1))
    tipe_keyword = request.args.get('tipe_keyword')
    keyword = request.args.get('keyword')
    sort = request.args.get('sort')
    tipe_sort = request.args.get('tipe_sort')
    range0 = request.args.get('range0')
    range1 = request.args.get('range1')
    range2 = request.args.get('range2')

    return TRANSAKSI_D.get_all_transaksi_detail(
    limit=limit,
    page=page,
    tipe_keyword=tipe_keyword,
    keyword=keyword,
    sort=sort,
    tipe_sort=tipe_sort,
    range0 = range0,
    range1 = range1,
    range2 = range2
    )

def create_transaksi_detail():
    transaksi_id = request.form.get('transaksi_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')
    harga = request.form.get('harga')

    validated = for_validation_transaksi_detail (transaksi_id,barang_id,kuantitas,harga)
    if validated is not None :
        return validated,404
    TRANSAKSI_D.create_transaksi_detail(transaksi_id,barang_id,kuantitas,harga)
    return '',200
    
def pick_id_transaksi_detail(id):
    get_id = TRANSAKSI_D.pick_id_transaksi_detail(id)
    if get_id is None :
        return '', 404
    return TRANSAKSI_D.pick_id_transaksi_detail(id)
    
def delete_transaksi_detail(id):
    get_id = TRANSAKSI_D.pick_id_transaksi_detail(id)
    if get_id is None:
        return '', 404
    TRANSAKSI_D.delete_transaksi_detail(id)
    return '',200
    
def editt_transaksi_detail(id): 
    if TRANSAKSI_D.pick_id_transaksi_detail(id) is None:
        return '' , 404
    transaksi_id = request.form.get('transaksi_id')
    barang_id = request.form.get('barang_id')
    kuantitas = request.form.get('kuantitas')
    harga = request.form.get('harga')

    validated = for_validation_transaksi_detail (transaksi_id,barang_id,kuantitas,harga)
    if validated is not None :
        return validated,404
    TRANSAKSI_D.edit_transaksi_detail(id,transaksi_id,barang_id,kuantitas,harga)
    return '', 200
