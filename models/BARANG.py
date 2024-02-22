from static.for_connectionDB import koneksidatabase

def get_all_data_barang (page : int, limit : int, keyword: str = None):
    '''
    melakukan eksekusi paginasi secara default dan menambahkan mekanisme search query apabila dibutuhkan dan kemudian mengembalikan data sesuai dengan 
    yang ada di database 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""

        if keyword is not None:
            whereKeyword = " WHERE nama_barang ilike %(keyword)s "

        query = f"""
        SELECT id,nama_barang,deskripsi,harga,stok,kategori_id 
        FROM barang 

        {whereKeyword}

        limit %(limit)s 
        offset %(offset)s

        """
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = '%'+keyword+'%'

        connection.execute(query,values)
        barangg = connection.fetchall()
        barang_baru = []
        for barang in barangg :
            baranggg = {
                    'id' : barang [0],
                    'nama_barang': barang [1],
                    'deskripsi' : barang [2],
                    'harga' : barang [3],
                    'stok' : barang [4],
                    'kategori_id' : [5],
            }
            barang_baru.append(baranggg)
        
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally: 
        connection.close()
    return barang_baru


def create_barang (nama_barang :str, deskripsi : str , harga :int , stok : int , kategori_id : int):
    '''
    membuat koneksi database untuk membuat barang
    '''
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
    '''
    mengambil id, nama_barang, deskripsi, harga, stok, kategori_id berdasarkan id yang dinginkan
    '''
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
        return 
    return{
        'id': barang [0],
        'nama_barang' : barang [1],
        'deskripsi' : barang [2],
        'harga' : barang [3],
        'stok' : barang [4],
        'kategori_id' : barang [5]
    }

def delete_barang (id):
    '''
    menghapus barang dengan memasukkan id yang dinginkan
    '''
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
    '''
    mengedit dalam tabel barang yang berisi nama_barang, deskripsi, harga, stok, kategori_id dengan memasukkan id yang dibutuhkan
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE barang SET nama_barang =%s, deskripsi =%s, harga =%s, stok =%s, kategori_id =%s WHERE id = %s',(nama_barang,deskripsi,harga,stok,kategori_id,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

def update_stok (stok : str , id : str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE barang SET stok = stok + %s where id = %s',(stok,id))
        koneksidatabase.commit()
    except Exception as e :
        raise e 
    finally: 
        connection.close()

def update_kuantitas (stok : int, id : int):
    connection = koneksidatabase.cursor()
    try : 
        connection.execute('UPDATE barang SET stok = %s where id = %s',(stok,id))
    except Exception as e :
        raise e 
    finally:
        connection.close()