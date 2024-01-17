from static.for_connectionDB import koneksidatabase

def get_all_transaksi_detail (page : int, limit : int, keyword: str = None):
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""

        if keyword is not None:
            whereKeyword = " WHERE transaksi_id ilike %(keyword)s "

        query = f"""
        SELECT id,transaksi_id,barang_id,kuantitas,harga FROM transaksi_detail 

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
        connection.close()
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