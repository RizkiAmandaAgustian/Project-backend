from for_connectionDB import koneksidatabase

def get_all_data_barang(page: int, limit: int, keyword: str = None, sort: str = None, tipe_data_sort: str = "asc", range1 : int = 0, range2 : int = 0):
    """
    Melakukan eksekusi paginasi secara default dan menambahkan mekanisme search query apabila dibutuhkan dan kemudian mengembalikan data sesuai dengan
    yang ada di database
    bagian def diatas tulisan ini adalah nilai default yang bisa kita pakai di controller contoh di bagian tipe_data_sort
    """
    connection = koneksidatabase.cursor()
    try:
        page = (page - 1) * limit

        wheres = [] #dibuat string kosong agar kalau nanti muncul data akan ditampung dahulu
        if keyword is not None and keyword != '':
            wheres.append(" nama_barang ILIKE %(keyword)s ") #jika keyword terisi akan dieksekusi

        sorting = ""

        
        if sort is not None or sort != '': #jika sort tidak kosong atau tidak berisi string kosong
            if tipe_data_sort not in ['asc','desc']:#membuat whitelist asc dan desc untuk pengurutan data
                raise ValueError("hanya boleh asc atau desc")

            if sort not in ['id','harga','stok']: #kolom yang diseduiakan untuk di sorting
                raise ValueError('kolom tidak ada di database') #jika tidak ada muncul eror 
            sorting = f" ORDER BY {sort} {tipe_data_sort}" #jika data ada maka kode akan dieksekusi

            
        if range1 is not None and range1 != '' and range2 is not None and range2 != '': #jika range terisi maka akan terisi angka jika kosong akan terskip hanya Where keyword saja
            wheres.append("harga between %(range1)s and %(range2)s") 

        
        #wheres = []
        where =""
        if len(wheres) > 0:
            where =" Where " + " AND ".join(wheres)

        '''
        Where nya otomatis nambah ketika ada ketika ada kondisi semisal keyword dia otomatis nambah 
        nama_barang ILIKE %(keyword)s
        kalo keyword tidak terisi dia beralih ke range 1 dan 2 dan menggunakan where juga
        apa bila 2 kondisi terpenuhi where otomatis didepan untuk keyword dan AND menjadi penggabung index yang ada di wheres
        karena dasarnya dia ditampung di Wheres jadi AND akan menjadi penghubung kode sql dan otomatis terhubung dengan .join(wheres)
        '''

        '''KALO MASIH BINGUNG WHERE + AND.JOIN(WHERES) DICOPAS KE I.D.E online python terus di run
        myTuple = ['kondisi1']
        where = ''
        if len(myTuple) > 0:
                    where =" Where " + " AND ".join(myTuple)

        print(where)

        myTuple = ['kondisi1','kondisi2']
        where = ''
        if len(myTuple) > 0:
                    where =" Where " + " AND ".join(myTuple)

        print(where)

        myTuple = ['kondisi1','kondisi2','kondisi3']
        where = ''
        if len(myTuple) > 0:
                    where =" Where " + " AND ".join(myTuple)

        print(where)

        myTuple = ['kondisi1','kondisi2','kondisi3','kondisi4']
        where = ''
        if len(myTuple) > 0:
                    where =" Where " + " AND ".join(myTuple)

        print(where)

        myTuple = ['kondisi1','kondisi2','kondisi3','kondisi4','kondisi5']
        where = ''
        if len(myTuple) > 0:
                    where =" Where ".join(myTuple) + " AND "

        print(where)
                '''

        query = f"""
            SELECT id, nama_barang, deskripsi, harga, stok, kategori_id
            FROM barang
            {where}
            {sorting}
            LIMIT %(limit)s
            OFFSET %(offset)s
        """
        print(query)
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = '%'+keyword+'%'
        if range1 is not None and range2 is not None :
            values['range1'] = range1
            values['range2'] = range2
        #kalau inputan harus ditegaskan value nya masuk kedalam value variabel apa
        '''
         SELECT id, nama_barang, deskripsi, harga, stok, kategori_id
            FROM barang
             Where  nama_barang ILIKE %(keyword)s  AND harga between %(range1)s and %(range2)s
             ORDER BY id asc
            LIMIT %(limit)s
            OFFSET %(offset)s
        kalau semua permintaan data diisi akan menghasilkan data diatas
        '''
            
        connection.execute(query, values) #eksekusi kode yang ada yaitu query dan values nya
        barangg = connection.fetchall() #ambil semua data yang ada 
        barang_baru = [] #buat list kosong
        for barang in barangg: #lakukan perulangan untuk mengambil semua data 
            baranggg = {
                "id": barang[0],
                "nama_barang": barang[1],
                "deskripsi": barang[2],
                "harga": barang[3],
                "stok": barang[4],
                "kategori_id": barang[5]
            }
            barang_baru.append(baranggg) #proses penambahan list barang_baru dari hasil for looping dan baranggg

        koneksidatabase.commit() #lalu hasilnya di commit ke database
    except Exception as e:
        koneksidatabase.rollback() #jika hasilnya salah maka akan di rollback
        raise e #dan dimunculkan eror nya
    finally:
        connection.close() #setelah itu koneksi ke database nya ditutup 
    return barang_baru #return hasil dari list data yang sudah baru 




def create_barang (nama_barang :str, deskripsi : str , harga :int , stok : int , kategori_id : int):
    '''
    membuat koneksi database untuk membuat barang
    '''
    connection = koneksidatabase.cursor() #memulai koneksi ke database
    try:
        connection.execute('INSERT INTO barang (nama_barang,deskripsi,harga,stok,kategori_id) VALUES (%s,%s,%s,%s,%s)',(nama_barang,deskripsi,harga,stok,kategori_id)) 
        #memasukkan ke database sesuai dengan value inputan yang diberikan di kontroller
        koneksidatabase.commit() #commit ke database
    except Exception as e :
        koneksidatabase.rollback() #rollback jika ditemukan eror
        raise e #munculkan eror yang ada
    finally:
        connection.close() #tutup koneksi ke database

def pick_id_barang (id):
    '''
    mengambil id, nama_barang, deskripsi, harga, stok, kategori_id berdasarkan id yang dinginkan
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id, nama_barang, deskripsi, harga, stok, kategori_id from barang where id = %s',(id,))
        barang = connection.fetchone() #mengambil 1 data 
        koneksidatabase.commit()#commit ke database
    except Exception as e :
        koneksidatabase.rollback()#rollback jika ditemukan eror
        raise e #munculkan eror yang ada
    finally :
        connection.close()#tutup koneksi ke database
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
    '''
    menghapus barang dengan memasukkan id yang dinginkan
    '''
    connection = koneksidatabase.cursor() #memulai koneksi database
    try:
        connection.execute('DELETE from barang where id = %s',(id,)) #menghapus data dengan memasukkan inputan id barang tersebut
        koneksidatabase.commit() #commit ke database
    except Exception as e :
        koneksidatabase.rollback() #rollback jika terjadi eror
        raise e #munculkan erornya
    finally :
        connection.close()#tutup koneksi ke database 

def edit_barang (id,nama_barang :str, deskripsi : str , harga :int , stok : int , kategori_id : int):
    '''
    mengedit dalam tabel barang yang berisi nama_barang, deskripsi, harga, stok, kategori_id dengan memasukkan id yang dibutuhkan
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE barang SET nama_barang =%s, deskripsi =%s, harga =%s, stok =%s, kategori_id =%s WHERE id = %s',(nama_barang,deskripsi,harga,stok,kategori_id,id))
        #memasukkan edit barang sesuai dengan inputan namun dengan mencocokkan id barang yang ingin diganti 
        koneksidatabase.commit()#commit ke database
    except Exception as e :
        koneksidatabase.rollback() #rollback jika ditemukan eror
        raise e #munculkan erornya 
    finally : 
        connection.close() #tutup koneksi ke database 

def tambah_stok (stok : str , id : str):
    #mengedit stok barang yang ada
    connection = koneksidatabase.cursor() #memulai koneksi ke database
    try:
        connection.execute('UPDATE barang SET stok = stok + %s where id = %s',(stok,id)) 
        #update untuk mengedit stok barang dengan mekanisme stok barang sekarang + dengan inputan yang ingin dimasukkan dan jangan lupa memasukkan id barang nya
        koneksidatabase.commit()
    except Exception as e :
        raise e 
    finally: 
        connection.close()

def update_kuantitas (stok : int, id : int):
    connection = koneksidatabase.cursor()
    try : 
        connection.execute('UPDATE barang SET stok = %s where id = %s',(stok,id))
        #update untuk mengedit stok barang dengan inputan yang ingin dimasukkan dan jangan lupa memasukkan id barang nya
        koneksidatabase.commit()
    except Exception as e :
        raise e 
    finally:
        connection.close()