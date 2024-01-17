from models import KATEGORI
from flask import request
from controllers.for_validate import for_validation_kategori

def get_all_data_kategori():
    limit = int(request.args.get("limit", 5))
    page = int(request.args.get("page", 1))

    return KATEGORI.get_all_data_kategori(
        limit=limit,
        page=page,
    )

def create_kategori():
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None :
        return validated,404
    KATEGORI.create_kategori(label)
    return '',200

def pick_id_kategori(id):
    get_id = KATEGORI.pick_id_kategori(id)
    if get_id is None :
        return '', 404
    return KATEGORI.pick_id_kategori(id)

def delete_kategori(id):
    get_id = KATEGORI.pick_id_kategori(id)
    if get_id is None:
        return '', 404
    KATEGORI.delete_kategori(id)
    return '',200

def editt_kategori(id): 
    if KATEGORI.pick_id(id) is None:
        return '' , 404
    label = request.form.get('label')
    validated = for_validation_kategori (label)
    if validated is not None:
        return validated,404
    KATEGORI.edit_kategori(id,label)
    return '', 200