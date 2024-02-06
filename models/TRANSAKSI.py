from static.for_connectionDB import koneksidatabase
from flask_jwt_extended import get_jwt_identity

def get_all_data_transaksi (page : int, limit : int, keyword: str = None):
    '''
    menentukan paginasi dan keyword apabila keryword terisi maka akan melakukan pencarian apabila kosong akan melakukan menampilkan data dengan sistem paginasi yang diatur di controller 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""

        if keyword is not None:
            whereKeyword = " WHERE nama_lengkap ilike %(keyword)s "

        query = f"""
        SELECT id, nama_lengkap, alamat, tanggal_transaksi, user_id FROM transaksi 

        {whereKeyword}

        limit %(limit)s 
        offset %(offset)s

        """
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = '%'+keyword+'%'

        connection.execute(query,values)
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
        connection.close()
    return new_data


def create_transaksi (nama_lengkap :str, alamat : str , user_id :int):
    '''
    memasukkan nama_lengkap,alamat,user_id kedalam tabel transaksi 
    '''
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
    '''
    mengambil id transaksi 
    '''
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
    '''
    menghapus transaksi berdasarkan id 
    '''
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
    '''
    mengedit transaksi berdasarkan id 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE transaksi SET nama_lengkap =%s, alamat =%s, user_id =%s WHERE id = %s',(nama_lengkap,alamat,user_id,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

def coba_transaksi(nama_lengkap,alamat,user_id):
    '''
    memasukkan nama_lengkap,alamat,user_id tanpa commit karena komit dilakukan di controller 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO transaksi (nama_lengkap,alamat,user_id) VALUES (%s,%s,%s) RETURNING id',(nama_lengkap,alamat,user_id)) 
        return connection.fetchone()[0] #berpengaruh pada data yang akan kita ambil di bagian returning
    except Exception as e :
        raise e 
    finally: 
        connection.close()
