from static.for_connectionDB import koneksidatabase

def get_all_data_keranjang (page : int, limit : int, keyword: str = None):
    '''
    menentukan paginasi dan keyword apabila keryword terisi maka akan melakukan pencarian apabila kosong akan melakukan menampilkan data dengan sistem paginasi yang diatur di controller 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""

        if keyword is not None:
            whereKeyword = " WHERE nama_barang ilike %(keyword)s "

        query = f"""
        SELECT id,user_id,barang_id,kuantitas 
        FROM keranjang 

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
    finally: 
        connection.close()
    return new_data


def create_keranjang (user_id :int, barang_id : int, kuantitas : int):
    '''
    memasukkan user_id,barang_id,kuantitas ke tabel keranjang 
    '''
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
    '''
    mengambil id keranjang 
    '''
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
    '''
    menghapus keranjang dengan id yang sama dengan yang dimasukkan 
    '''
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
    '''
    menghapus keranjang dengan id yang sama dengan yang dimasukkan 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE keranjang SET user_id =%s, barang_id =%s, kuantitas =%s  WHERE id = %s',(user_id,barang_id,kuantitas,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

def coba_pick_id_keranjang (id):
    '''
    mengambil id keranjang 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('select k.id, user_id, barang_id, kuantitas, b.harga from keranjang k join barang b on b.id = k.barang_id where k.id= %s',(id,))
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
        'kuantitas' : laptop [3],
        'harga': int(laptop[4])
    }