from models import USERS
from flask import request
from flask_jwt_extended import create_access_token
from controllers.for_validate import for_validation_users

def user_login ():
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        login_user = USERS.login_users(username,password)
        if login_user:
            accses_token = create_access_token(identity=username)
            return{'LOGIN BERHASIL DAN TOKEN ANDA': accses_token}
        return{'USERNAME ATAU PASSWORD SALAH'},404

def create_users():
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
