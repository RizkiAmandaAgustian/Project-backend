from static.for_connectionDB import koneksidatabase
def login_users (username,password):
    koneksi = koneksidatabase.cursor()
    try:
        koneksi.execute('SELECT * from users WHERE username = %s AND password = %s',(username,password))
        masuk = koneksi.fetchone()
        if masuk is None:
            return None
        return{
            'username': masuk[0],
            'password': masuk [1]
        }
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally: 
        koneksi.close()


def create_users (username :str, password : str , nama_lengkap : str):
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
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from users where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_users (id : int,username : str, password : str , nama_lengkap : str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE users SET username =%s, password = %s, nama_lengkap = %s WHERE id = %s',(username,password,nama_lengkap,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()
