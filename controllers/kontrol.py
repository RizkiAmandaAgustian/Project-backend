from flask import request
from flask_jwt_extended import create_access_token
from controllers.for_validate import for_validation_kategori,for_validation_barang,for_validation_keranjang,for_validation_transaksi,for_validation_transaksi_detail,for_validation_users
from models import for_mechanism,USERS,KATEGORI,BARANG,KERANJANG,TRANSAKSI,TRANSAKSI_D
import time
import os


#kategori



#Barang


#KERANJANG



#TRANSAKSI 



#TRANSAKSI DETAIL



def paginasi ():
    limit = int(request.args.get("limit", 5))
    page = int(request.args.get("page", 1))

    return for_mechanism.paginasi(
        limit=limit,
        page=page,
    )

def upload_gambar(id):
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    if file.content_type not in [
        "image/jpeg",
        "image/jpg",
        "image/webp",
        "image/png",
    ]:
        return "File type not allowed"
    
    
    file = request.files["file"]
    location = "static/uploads/" + str(time.time()) + "_" + file.filename
    file.save(location)
    
    
    for_mechanism.upload_gambar(location,id)
    return '',200

# def edit_gambar():
#     if "file" not in request.files:
#         return "No file part"

#     file = request.files["file"]

#     if file.filename == "":
#         return "No selected file"
    
#     location_new = None
#     # Hapus file lama

#     # Simpan file baru
#     location_new = "static/uploads/" + str(time.time()) + "_" + file.filename
#     file.save(location_new)

#     if location_new is not None:
#             os.remove(location_new)
#     return for_mechanism.edit_gambar, 200

def get_id_gambar(id):
    ambilgambar = for_mechanism.pick_id_gambar(id)
    if ambilgambar is None : 
        return None
    return for_mechanism.pick_id_gambar(id)

def hapus_gambar(id):
    hapus = for_mechanism.pick_id_gambar(id)
    if hapus is None :
        return None
    return for_mechanism.hapus_gambar(id)


