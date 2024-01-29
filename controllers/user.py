from models import USERS
from flask import request
from flask_jwt_extended import create_access_token
from for_validate import for_validation_users,for_validation_users1
from flask_jwt_extended import get_jwt_identity

def user_login ():
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        login_user = USERS.login_users(username=username,password=password)
        print (login_user)
        if login_user:
            accses_token = create_access_token(identity={'username':login_user['username'],'id':login_user['id']})
            return{'Token': accses_token}
        return{'USERNAME ATAU PASSWORD SALAH'},404

def create_users():
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
    get_id = USERS.pick_id_users(id)
    if get_id is None :
        return '', 404
    return USERS.pick_id_users(id)

def delete_users(id):
    get_id = USERS.pick_id_users(id)
    if get_id is None:
        return '', 404
    USERS.delete_users(id)
    return '',200

def editt_users(id): 
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
