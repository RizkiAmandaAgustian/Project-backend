from flask import request
import os, time
from models import GAMBAR
from flask_jwt_extended import get_jwt_identity

def upload_gambar():
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian1': #validasi apakah yang login apakah Tian sebagai admin atau bukan
        return {'message':'ANDA BUKAN TIAN'},401
     
    if "file" not in request.files: #melakukan pengecekan apakah file adalah nama untuk pengupload an gambar
        return "No file part"

    file = request.files["file"] #variabel file digunakan untuk penamaan pengupload an 

    if file.filename == "" and file.filename is not None : #pengecekan apakah file berisi string kosong atau tidak
        return "No selected file"
    '''Penjelasan .filename 
    adalah atribut yang diberikan oleh Flask untuk objek berkas yang diunggah. Ketika Anda mengunggah berkas menggunakan formulir HTML, 
    atribut name dari elemen input file menjadi kunci untuk data berkas tersebut dalam objek request.files di Flask.

    Ketika Anda mengakses request.files["file"], Anda mendapatkan objek berkas yang berisi beberapa atribut, salah satunya adalah .filename. 
    Atribut ini berisi nama berkas asli saat diunggah oleh pengguna.

    Misalnya, jika pengguna mengunggah berkas dengan nama "gambar.jpg", maka nilai file.filename akan menjadi "gambar.jpg". 
    Jika tidak ada berkas yang dipilih oleh pengguna, nilai file.filename akan menjadi string kosong ("").

    Jadi, .filename bukanlah nilai yang diberikan secara default, tetapi nilainya bergantung pada nama berkas yang diunggah oleh 
    pengguna melalui formulir HTML.
    '''
    if file.content_type not in [ #pengecekan format
        "image/jpeg",
        "image/jpg",
        "image/webp",
        "image/png",
    ]:
        return "File type not allowed"
    
    
    file = request.files["file"]
    location = "static/uploads/" + str(time.time()) + "_" + file.filename #penamaan file upload an dna lokasi nya 
    file.save(location)#eksekusi penyimpanan file
    
    
    GAMBAR.upload_gambar(location)
    return '',200

def edit_gambar(id):
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian1':#validasi apakah yang login apakah Tian sebagai admin atau bukan
        return {'message':'ANDA BUKAN TIAN'},401
    if "file" not in request.files:#melakukan pengecekan apakah file adalah nama untuk pengupload an gambar
        return "No file part"

    file = request.files["file"]

    if file.filename == "" and file.filename is not None:#pengecekan apakah file berisi string kosong atau tidak
        return "No selected file"
    
    if file.content_type not in [ #pengecekan format
        "image/jpeg",
        "image/jpg",
        "image/webp",
        "image/png",
    ]:
        return "File type not allowed"
    '''Kurang berguna namun tidak dihapus untuk pembelajaran dan dokumentasi saja
    location_new = None
    Hapus file lama

    Simpan file baru
    location_new = "static/uploads/" + str(time.time()) + "_" + file.filename #lokasi baru penyimpanan
    file.save(location_new) 

    if location_new is not None:
        os.remove(location_new)
    '''
    GAMBAR.edit_gambar(id)
    return '',200

def get_id_gambar(id):
    ambilgambar = GAMBAR.pick_id_gambar(id)
    if ambilgambar is None : 
        return None
    return GAMBAR.pick_id_gambar(id)

def hapus_gambar(id):
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    hapus = GAMBAR.pick_id_gambar(id)
    if hapus is None :
        return None
    return GAMBAR.hapus_gambar(id)


