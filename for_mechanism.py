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

# TRANSAKSI
        
def get_all_data_transaksi ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id, nama_lengkap, alamat, tanggal_transaksi, user_id FROM transaksi ')
        result = connection.fetchall()
        new_data = []
        for transaksi in result :
            data_baru = {
                'id' : transaksi [0],
                'nama_lengkap': transaksi [1],
                'alamat' : transaksi [2],
                'tanggal_transaksi' : transaksi [3],
                'user_id' : transaksi [4],
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create_transaksi (nama_lengkap :str, alamat : str , user_id :int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO transaksi (nama_lengkap,alamat,user_id) VALUES (%s,%s,%s)',(nama_lengkap,alamat,user_id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_transaksi (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id, nama_lengkap, alamat, tanggal_transaksi, user_id from transaksi where id = %s',(id,))
        transaksi = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    if transaksi is None:
        return None
    return{
        'id': transaksi [0],
        'nama_lengkap' : transaksi [1],
        'alamat' : transaksi [2],
        'tanggal_transaksi' : transaksi [3],
        'user_id' : transaksi [4]
    }

def delete_transaksi (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from transaksi where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_transaksi (id,nama_lengkap :str, alamat : str , user_id :int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE transaksi SET nama_lengkap =%s, alamat =%s, user_id =%s WHERE id = %s',(nama_lengkap,alamat,user_id,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

#TRANSAKSI DETAIL

def get_all_data_transaksi_detail ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,transaksi_id,barang_id,kuantitas,harga FROM transaksi_detail')
        result = connection.fetchall()
        new_data = []
        for transaksi_detail in result :
            data_baru = {
                'id' : transaksi_detail [0],
                'transaksi_id': transaksi_detail [1],
                'barang_id': transaksi_detail [2],
                'kuantitas' : transaksi_detail [3],
                'harga' : transaksi_detail [4]
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create_transaksi_detail (transaksi_id :int, barang_id : int, kuantitas : int , harga : int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO transaksi_detail (transaksi_id,barang_id,kuantitas,harga) VALUES (%s,%s,%s,%s)',(transaksi_id,barang_id,kuantitas,harga))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_transaksi_detail (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,transaksi_id,barang_id,kuantitas,harga from transaksi_detail where id = %s',(id,))
        transaksi_detail = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    if transaksi_detail is None:
        return None
    return{
        'id' : transaksi_detail [0],
        'transaksi_id': transaksi_detail [1],
        'barang_id': transaksi_detail [2],
        'kuantitas' : transaksi_detail [3],
        'harga' : transaksi_detail [4]
    }

def delete_transaksi_detail (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from transaksi_detail where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_transaksi_detail (id,transaksi_id :int, barang_id : int, kuantitas : int , harga : int):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE transaksi_detail SET transaksi_id =%s, barang_id =%s, kuantitas =%s,  harga = %s WHERE id =%s',(transaksi_id,barang_id,kuantitas,harga,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()