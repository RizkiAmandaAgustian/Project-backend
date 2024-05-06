from models import USERS
from flask import request
from flask_jwt_extended import create_access_token
from for_validate import for_validation_users,for_validate_username
from flask_jwt_extended import get_jwt_identity
from flask_bcrypt import Bcrypt
from flask_bcrypt import generate_password_hash
from datetime import timedelta

def user_login ():
        '''
        Fungsi controllers untuk memasukkan username dan password apakah sama dengan yang ada di database
        login_user = USERS.login_users untuk mendapatkan data username dan password yang sudah di eksekusi di modul yang berada dalam folder models.USERS
        jika login_user berhasil maka akan mendapatkan akses token dan akan mengambil username dan id sesuai yang ada di database
        '''
        username = request.form.get('username', None)# proses memasukkan username kedalam inputan
        password = request.form.get('password', None)# proses memasukkan password kedalam inputan

        login_user = USERS.login_users(username=username) # melakukan pengecekan terhadap username yang berada di database melalui models 
        bkrip = Bcrypt() #membuat variabel bkrip sebagai penampung fungsi Bcrypt()
        if bkrip.check_password_hash(login_user['password'],password):
            #melakukan pengecekan dengan mekanisme mengambil password yang sudah di hash dari database dengan yang dimasukkan di inputan
            accses_token = create_access_token(identity={'username':login_user['username'],'id':login_user['id']},expires_delta=timedelta(hours=1))
            #membuat akses token yang didalamnya terdapat identitas username dan id nya serta melakukan set expired selama kurun waktu tertentu
            return{'Token': accses_token} #jika benar akan menghasilkan token
        return{'USERNAME ATAU PASSWORD SALAH'},404

def create_users():
    '''
    fungsi controllers untuk membuat users guna untuk login dan mendapatkan akses token, dalam bagian ini jika username tidak memiliki isi Tian maka kode tidak
    akan di eksekusi untuk menambah users.
    Setelah kita login sebagai tian isi username password dan nama lengkap dan akan di validasi apakah username kita tidak value kosong atau string kosong
    setelah mengisi dan tidak ada yang kosong maka akan dilanjutkan ke models.USERS.create_users untuk disambungkan ke database agar username dan password 
    bisa disimpan disana 
    '''
    username = request.form.get('username') #memasukkan username   
    password = request.form.get('password') #memasukkan password
    nama_lengkap = request.form.get('nama_lengkap')#memasukkan nama lengkap 
    validated = for_validation_users (username,password,nama_lengkap) #melakukan pengecekan terhadap username, password dan nama lengkap
    if validated is not None : # pengecekan tadi akan menghasilkan jumlah eror apabila muncul jumlah eror akan dihasilkan dibawahnya
        return validated,400 # apabila eror muncul akan dimunculkan disini 
    validated_username = for_validate_username(username)#VALIDASI UNTUK MENGECEK APAKAH DATA TERSEBUT SUDAH ADA DI DATABASE ATAU BELUM
    if validated_username is not None: 
        return validated_username,400 #JIKA SUDAH ADA MAKA AKAN MENGHASILKAN EROR
    bkrip = Bcrypt () # apabila sudah dilakukan pengecekan bkrip disini berguna untuk menampung fungsi Bcrypt()
    hashing = bkrip.generate_password_hash(password).decode('utf-8') #mulai hashing password
    USERS.create_users(username,hashing,nama_lengkap) #masukkan username password yang sudah di hashing ke database
    return '',201

def pick_id_users(id):
    '''
    pick_id_users untuk mengambil suatu data di database dengan menambahkan id pada route pemanggilan data
    '''
    get_id = USERS.pick_id_users(id)
    if get_id is None :
        return '', 404
    return USERS.pick_id_users(id)

def delete_users(id):
    '''
    delete_users untuk menghapus suatu data di database dengan menambahkan id pada route pemanggilan data
    sebelum menghapus data dilakukan pengecekan terlebih dahulu dengan USERS.pick_id_users apabila ada data yang dimaksud lantas bisa kita hapus
    '''
    get_id = USERS.pick_id_users(id)
    if get_id is None:
        return '', 404
    USERS.delete_users(id)
    return '',200

def editt_users(id): 
    '''
    editt_users untuk mengedit suatu data dengan menambahkan id pada route pemanggilan data
    pertama dilakukan pengecekan USERS.pick_id_users untuk memastikan data memang ada
    setelah itu kita isi semua data yang ingin diubah seperti username,password dan nama lengkap dan kemudian divalidasi untuk memastikan data telah terisi
    setelah itu dilakukan eksekusi ke database melalui USERS.edit_users
    '''
    if USERS.pick_id_users(id) is None:
        return '' , 404
    username = request.form.get('username')#memasukkan username
    password = request.form.get('password')#memasukkan password
    nama_lengkap = request.form.get('nama_lengkap')#memasukkan nama lengkap
    validated = for_validation_users (username,password, nama_lengkap) #di validasi dulu apakah kosong atau string kosong atau tidak 
    if validated is not None:
        return validated,404 #jika kosong akan muncul eror seperti eror handling yang ada
    validated_username = for_validate_username(username)#VALIDASI UNTUK MENGECEK APAKAH DATA TERSEBUT SUDAH ADA DI DATABASE ATAU BELUM
    if validated_username is not None: 
        return validated_username,400 #JIKA SUDAH ADA MAKA AKAN MENGHASILKAN ERORS
    brkip = Bcrypt() #jika tidak eror lanjut membuat variabel untuk fungsi Bcrypt()
    pwhash = brkip.generate_password_hash(password).decode('utf-8') #buat variabel untuk menampung password yang sebelumnya yang kemudian di hashing
    USERS.edit_users(id=id,username=username,pwhash=pwhash,nama_lengkap=nama_lengkap)
    return '', 200
