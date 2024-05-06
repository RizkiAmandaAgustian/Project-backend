from for_connectionDB import koneksidatabase
import os
def login_users (username:str):
    '''
    login_users untuk mengambil data username dan password yang berada di database
    dan di return username(0) dan id (2) untuk menambil data sesuai dengan urutan eksekusi kode sql dalam kode koneksi.execute yaitu 
    username berada pada posisi 0 dan id pada posisi ke 2  
    '''
    koneksi = koneksidatabase.cursor()
    try:
        koneksi.execute('SELECT username,password,id from users WHERE username = %s ',(username,))
        masuk = koneksi.fetchone()
        if masuk is None:
            return None
        return{'username': masuk[0],'password': masuk [1],'id': masuk[2]}
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally: 
        koneksi.close()


def create_users (username :str, password : str , nama_lengkap : str):
    '''
    create_users untuk melakukan komunikasi ke database guna menambahkan users 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO users (username,password,nama_lengkap) VALUES (%s,%s,%s)',(username,password,nama_lengkap))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_users (id : int):
    '''
    pick_id_users untuk mengambil suatu data users di database dengan id yang valid
    apabila data tidak kosong maka akan di return sesuai dengan isi yang di eksekusi dan return yang dituliskan  
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,username,password from users where id = %s',(id,))
        laptop = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    if laptop is None:
        return None
    return{
        'id': laptop [0],
        'username' : laptop [1],
        'password' : laptop [2]
    }

def delete_users (id : int):
    '''
    pick_id_users untuk mengambil suatu data users di database dengan id yang valid 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from users where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_users (id : int,username : str, pwhash : str , nama_lengkap : str):
    '''
    edit_users untuk mengedit/update suatu data users di database dengan id yang valid 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE users SET username =%s, password = %s, nama_lengkap = %s WHERE id = %s',(username,pwhash,nama_lengkap,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()
