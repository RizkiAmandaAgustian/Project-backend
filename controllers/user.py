from models import USERS
from flask import request
from flask_jwt_extended import create_access_token
from for_validate import for_validation_users,for_validation_users1
from flask_jwt_extended import get_jwt_identity

def user_login ():
        '''
        Fungsi controllers untuk memasukkan username dan password apakah sama dengan yang ada di database
        login_user = USERS.login_users untuk mendapatkan data username dan password yang sudah di eksekusi di modul yang berada dalam folder models.USERS
        jika login_user berhasil maka akan mendapatkan akses token dan akan mengambil username dan id sesuai yang ada di database
        '''
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        login_user = USERS.login_users(username=username,password=password)
        print (login_user)
        if login_user:
            accses_token = create_access_token(identity={'username':login_user['username'],'id':login_user['id']})
            return{'Token': accses_token}
        return{'USERNAME ATAU PASSWORD SALAH'},404

def create_users():
    '''
    fungsi controllers untuk membuat users guna untuk login dan mendapatkan akses token, dalam bagian ini jika username tidak memiliki isi Tian maka kode tidak
    akan di eksekusi untuk menambah users.
    Setelah kita login sebagai tian isi username password dan nama lengkap dan akan di validasi apakah username kita tidak value kosong atau string kosong
    setelah mengisi dan tidak ada yang kosong maka akan dilanjutkan ke models.USERS.create_users untuk disambungkan ke database agar username dan password 
    bisa disimpan disana 
    '''
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
    print(cek_user)
    username = request.form.get('username')
    password = request.form.get('password')
    nama_lengkap = request.form.get('nama_lengkap')
    validated = for_validation_users (username,password,nama_lengkap)
    if validated is not None :
        return validated,404
    USERS.create_users(username,password,nama_lengkap)
    return '',200

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
    cek_user=get_jwt_identity()
    if cek_user ['username'] != 'Tian':
        return {'message':'ANDA BUKAN TIAN'},401
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
    username = request.form.get('username')
    password = request.form.get('password')
    nama_lengkap = request.form.get('nama_lengkap')
    validated = for_validation_users (username,password, nama_lengkap)
    if validated is not None:
        return validated,404
    USERS.edit_users(id,username,password, nama_lengkap)
    return '', 200
