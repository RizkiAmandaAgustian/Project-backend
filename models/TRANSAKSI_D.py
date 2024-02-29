from for_connectionDB import koneksidatabase

def get_all_transaksi_detail (page : int, limit : int, keyword: str = None,sort : str = None, tipe_sort : str = None, range1 : int = 0, range0 : str = None, range2 : int = 0, tipe_keyword : str = None):
    '''
    menentukan paginasi dan keyword apabila keryword terisi maka akan melakukan pencarian apabila kosong akan melakukan menampilkan data dengan sistem paginasi yang diatur di controller 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""
        rangedata = ''
        container = []
        whitelist_transaksiD = ['id','transaksi_id','barang_id','kuantitas','harga']
        whitelist_tipe = ['asc','desc']
        #BUAT WHITELIST DAN RANGE HARGA

        if keyword is not None:
            if tipe_keyword not in whitelist_transaksiD:
                ValueError('data tidak ada dalam whitelist')    
            container.append( F" {tipe_keyword} = %(keyword)s ")

        if sort is not None and sort != '':
            if sort not in whitelist_transaksiD :
                ValueError('Data yang diinginkan tidak ada coba untuk memasukkan'.join(whitelist_transaksiD))
            if tipe_sort not in whitelist_tipe:
                ValueError('Data yang diinginkan tidak ada coba untuk memasukkan'.join(whitelist_tipe)) 
            rangedata = (F'ORDER BY {sort} {tipe_sort}')
        
        if range0 is not None :
            if range0  not in whitelist_transaksiD :
                ValueError ('Data tidak ada coba pastikan anda memasukkan salah satu dari '.join(whitelist_transaksiD))
            container.append(f" {range0} BETWEEN %(range1)s AND %(range2)s")

        if len(container)>0 :
            container_data = "Where " + " AND ".join(container)


        query = f"""
        SELECT id,transaksi_id,barang_id,kuantitas,harga FROM transaksi_detail 

        {container_data}

        {rangedata}


        limit %(limit)s 
        offset %(offset)s

        """
        print(query)
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = keyword
            
        if range0 is not None:
            values['range1'] = range1
            values['range2'] = range2


        

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
    '''
    menambah transaksi_id,barang_id,kuantitas,harga ke transaksi detail
    '''
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
    '''
    mengambil id transaksi detail
    '''
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
    '''
    mengahpus transaksi detail dengan berdasarkan id 
    '''
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
    '''
    mengahpus transaksi detail dengan berdasarkan id 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE transaksi_detail SET transaksi_id =%s, barang_id =%s, kuantitas =%s,  harga = %s WHERE id =%s',(transaksi_id,barang_id,kuantitas,harga,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()

def coba_transaksi (transaksi_id,barang_id,kuantitas,harga): 
    '''
    memasukkan transaksi detail tanpa commit karena commit dilakukan di controller 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO transaksi_detail (transaksi_id,barang_id,kuantitas,harga) VALUES (%s,%s,%s,%s)',(transaksi_id,barang_id,kuantitas,harga))
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()