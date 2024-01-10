from for_connectionDB import koneksidatabase



#USERS

def login (username,password):
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

#KATEGORI

def get_all_data_kategori ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,label FROM kategori')
        result = connection.fetchall()
        new_data = []
        for kategori in result :
            data_baru = {
                'id' : kategori [0],
                'label': kategori [1],
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create_kategori (label :str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO kategori (label) VALUES (%s)',(label,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_kategori (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,label from kategori where id = %s',(id,))
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
        'label' : laptop [1],
    }

def delete_kategori (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from kategori where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_kategori (id,label : str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE kategori SET label =%s WHERE id = %s',(label,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

#BARANG
        
def get_all_data_barang ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,nama_barang,deskripsi,harga,stok,kategori_id FROM barang ')
        result = connection.fetchall()
        new_data = []
        for barang in result :
            data_baru = {
                'id' : barang [0],
                'nama_barang': barang [1],
                'deskripsi' : barang [2],
                'harga' : barang [3],
                'stok' : barang [4],
                'kategori_id' : [5],
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create_barang (nama_barang :str, deskripsi : str , harga :int , stok : int , kategori_id : int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO barang (nama_barang,deskripsi,harga,stok,kategori_id) VALUES (%s,%s,%s,%s,%s)',(nama_barang,deskripsi,harga,stok,kategori_id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_barang (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id, nama_barang, deskripsi, harga, stok, kategori_id from barang where id = %s',(id,))
        barang = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    if barang is None:
        return None
    return{
        'id': barang [0],
        'nama_barang' : barang [1],
        'deskripsi' : barang [2],
        'harga' : barang [3],
        'stok' : barang [4],
        'kategori_id' : barang [5]
    }

def delete_barang (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from barang where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_barang (id,nama_barang :str, deskripsi : str , harga :int , stok : int , kategori_id : int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE barang SET nama_barang =%s, deskripsi =%s, harga =%s, stok =%s, kategori_id =%s WHERE id = %s',(nama_barang,deskripsi,harga,stok,kategori_id,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

#KERANJANG
        
def get_all_data_keranjang ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,user_id,barang_id,kuantitas FROM keranjang')
        result = connection.fetchall()
        new_data = []
        for keranjang in result :
            data_baru = {
                'id' : keranjang [0],
                'user_id': keranjang [1],
                'barang_id': keranjang [2],
                'kuantitas' : keranjang [3]
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create_keranjang (user_id :int, barang_id : int, kuantitas : int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO keranjang (user_id,barang_id,kuantitas) VALUES (%s,%s,%s)',(user_id,barang_id,kuantitas))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_keranjang (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,user_id,barang_id,kuantitas from keranjang where id = %s',(id,))
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
        'user_id' : laptop [1],
        'barang_id' : laptop [2],
        'kuantitas' : laptop [3]
    }

def delete_keranjang (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from keranjang where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_keranjang (id,user_id:int,barang_id:int,kuantitas:int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE keranjang SET user_id =%s, barang_id =%s, kuantitas =%s  WHERE id = %s',(user_id,barang_id,kuantitas,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()