from flask import request
import os, time
from models import GAMBAR

def upload_gambar():
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
    
    
    GAMBAR.upload_gambar(location)
    return '',200

def edit_gambar(id):
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"
    
    location_new = None
    # Hapus file lama

    # Simpan file baru
    location_new = "static/uploads/" + str(time.time()) + "_" + file.filename
    file.save(location_new)

    if location_new is not None:
            os.remove(location_new)
    return GAMBAR.edit_gambar(id), 200

def get_id_gambar(id):
    ambilgambar = GAMBAR.pick_id_gambar(id)
    if ambilgambar is None : 
        return None
    return GAMBAR.pick_id_gambar(id)

def hapus_gambar(id):
    hapus = GAMBAR.pick_id_gambar(id)
    if hapus is None :
        return None
    return GAMBAR.hapus_gambar(id)


