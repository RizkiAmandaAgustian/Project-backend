from models import KATEGORI,BARANG,TRANSAKSI
def for_validation_kategori (label):
    error = []
    if label is None :
        error.append('masukkan label laptop')
    # if support_thunderbolt is None :
    #     error.append('Masukkan apakah laptop seri ini support thunderbolt atau tidak')
    # else:
    #     if support_thunderbolt not in ['0','1']:
    #         error.append('masukkan 0 atau 1 sebagai penanda apakah laptop tersebut support thunderbolt atau tidak')
    if len (error)> 0 :
        return {'error':error}
    
def for_validation_barang (nama_barang, deskripsi, harga, stok, kategori_id):
    error = []
    if nama_barang is None or nama_barang == '':
        error.append('masukkan nama_barang')
    if harga is None or harga == '':
        error.append('masukkan harga')
    if deskripsi is None or deskripsi == '':
        error.append('masukkan deskripsi')
    if stok is None or stok == '':
        error.append('masukkan stok')
    if kategori_id is None or kategori_id == '':
        error.append('masukkan kategori_id')
    else:
        if KATEGORI.pick_id_kategori(kategori_id) is None:
            error.append("Kategori tidak ada di database")

    if len (error)>0:
        return {'error':error}
    
def for_validation_keranjang (barang_id, kuantitas):
    error = []
    # if user_id is None :
    #     error.append('masukkan user_id')
    if kuantitas is None or kuantitas == '' :
        error.append('masukkan kuantitas')
    if barang_id is None or barang_id == '' :
        error.append('masukkan barang_id')
    else:
        if BARANG.pick_id_barang(barang_id) is None:
            error.append ('id barang yang dimaksud tidak ada di database')
    if len (error)>0:
        return {'error':error}

def for_validation_transaksi (nama_lengkap, alamat, user_id):
    error = []
    if nama_lengkap is None or nama_lengkap == '' :
        error.append('masukkan nama_lengkap')
    if user_id is None or user_id == '' :
        error.append('masukkan user_id')
    if alamat is None or alamat == '' :
        error.append('masukkan alamat')
    if len (error)>0:
        return {'error':error}
    
def for_validation_transaksi_detail (transaksi_id, barang_id, kuantitas, harga):
    error = []
    if transaksi_id is None :
        error.append('masukkan transaksi_id')
    else:
        if TRANSAKSI.pick_id_transaksi(transaksi_id) is None:
            error.append ('transaksi id yang dimaksud tidak ada dalam database')
    if kuantitas is None :
        error.append('masukkan kuantitas')
    if barang_id is None :
        error.append('masukkan barang_id')
    else:
        if BARANG.pick_id_barang(barang_id) is None:
            error.append ('id barang yang dimaksud tidak ada di database')
    if harga is None :
        error.append('masukkan harga')
    if len (error)>0:
        return {'error':error}
    
def for_validation_users (username, password,nama_lengkap): #VALIDASI DISINI SESUAI DENGAN YANG INGIN DIGANTI DI DATABASE KALAU YANG INGIN DI EDIT 3 YA ISI 3
    error = []
    if username is None or username == '' :
        error.append('masukkan username')
    if password is None or password == '' :
        error.append('masukkan password')
    if nama_lengkap is None or nama_lengkap == '' :
        error.append('masukkan nama_lengkap')
    if len (error)>0:
        return {'error':error}
    
def for_validation_users1 (username, password): #VALIDASI DISINI SESUAI DENGAN YANG INGIN DIGANTI DI DATABASE KALAU YANG INGIN DI EDIT 3 YA ISI 3
    error = []
    if username is None or username == '' :
        error.append('masukkan username')
    if password is None or password == '' :
        error.append('masukkan password')
        return {'error':error}