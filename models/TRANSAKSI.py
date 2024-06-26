from for_connectionDB import koneksidatabase
from flask_jwt_extended import get_jwt_identity

def get_all_data_transaksi (page : int, limit : int, keyword: str = None, sorting : str = None,sort : str = None, tipe_sort : str = None):
    '''
    menentukan paginasi dan keyword apabila keryword terisi maka akan melakukan pencarian apabila kosong akan melakukan menampilkan data dengan sistem paginasi yang diatur di controller 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""
        container_data = []
        whitelist_user = ['user_id','alamat','nama_lengkap','id'] #memberikan daftar pilihan dalam bentuk tipe list apa yang bisa dicari
        tipedatawhitelist_user = ['asc','desc'] # memberikan pilihan urutan sortir desc atau asc



        if keyword is not None:
            container_data.append(" where nama_lengkap ilike %(keyword)s") #Where ditaruh disini karena order tidak membutuhkan Where ketika dipanggil
        

       
        if sort is not None and sort != '' : #jika data tidak kosong atau tidak berisi string kosong maka lakukan kode berikut
            if tipe_sort  not in tipedatawhitelist_user: #jika tipe sort tidak dalam tipedatawhitelist_user maka munculkan eror
                raise ValueError ('Tipe yang seharusnya dimasukkan adalah '+''.join(tipedatawhitelist_user))
            if sort not in whitelist_user: #jika sort tidak berada pada whitelist_user maka munculkan eror
                raise ValueError('Tipe yang harusnya dimasukkan adalah '+''.join(whitelist_user))
            container_data.append(F'ORDER BY {sort} {tipe_sort}')

        if len(container_data)>0:
            perintah = " ".join(container_data) #Tidak butuh AND karena Order by tidak memerlukan AND
            



        query = f"""
        SELECT id, nama_lengkap, alamat, tanggal_transaksi, user_id FROM transaksi 

        {perintah}

        limit %(limit)s 
        offset %(offset)s

        """
        print(query)
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
        #Returning id untuk mengambil id transaksi yang berguna untuk langsung memasukkan id transaksi ke transaksi detail
        return connection.fetchone()[0] #fetch atau pengambilan data di bagian returning berhubung yang diambil hanya 1 maka berisi 0
    except Exception as e :
        raise e 
    finally: 
        connection.close()
