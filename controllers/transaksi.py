from models import TRANSAKSI,BARANG,TRANSAKSI_D,KERANJANG
from flask import request
from for_validate import for_validation_transaksi
from flask_jwt_extended import get_jwt_identity
from for_connectionDB import koneksidatabase

def get_all_data_transaksi():
        '''
        get_all_data_barang mengambil semua data berdasarkan sistem paginasi dengan default 3 data dalam 1 halaman dan menggunakan keyword apabila ingin digunakan 
        '''
        limit = int(request.args.get("limit", 5))
        page = int(request.args.get("page", 1))
        sort = request.args.get('sort')
        keyword = request.args.get('keyword')
        tipe_sort = request.args.get('tipe_sort')

        return TRANSAKSI.get_all_data_transaksi(
        limit=limit,
        page=page,
        sort = sort,
        tipe_sort= tipe_sort,
        keyword=keyword
    )
def create_transaksi():
    '''
    membuat transaksi dengan memasukkan nama_lengkap, alamat dan user id
    '''
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    TRANSAKSI.create_transaksi(nama_lengkap,alamat,user_id)
    return '',200

def pick_id_transaksi(id):
    '''
    mengambil id transaksi 
    '''
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None :
        return '', 404
    return TRANSAKSI.pick_id_transaksi(id)

def delete_transaksi(id):
    '''
    mengapus transaksi berdasarkan dengan pengecekan id transaksi terlebih dahulu 
    '''
    get_id = TRANSAKSI.pick_id_transaksi(id)
    if get_id is None:
        return '', 404
    TRANSAKSI.delete_transaksi(id)
    return '',200

def editt_transaksi(id): 
    '''
    mengedit transaksi berdasarkan dengan pengecekan id transaksi terlebih dahulu 
    '''
    if TRANSAKSI.pick_id_transaksi(id) is None:
        return '' , 404
    nama_lengkap = request.form.get('nama_lengkap')
    alamat = request.form.get('alamat')
    user_id = request.form.get('user_id')

    validated = for_validation_transaksi (nama_lengkap,alamat,user_id)
    if validated is not None :
        return validated,404
    TRANSAKSI.edit_transaksi(id,nama_lengkap,alamat,user_id)
    return '', 200

def coba_transaksi():
    '''
    melakukan transaksi dan transaksi detail dalam 1 langkah eksekusi 
    memasukkan user id by token dan manual input nama_lengkap,alamat,cart_ids
    dan melakukan transaksi dan melakukan pengulangan dan melakukan transaksi detail 
    '''
    Connection = koneksidatabase.cursor()
    try:
        user_id = get_jwt_identity ()['id'] #id otomatis diambil terhadap siapa yang login dalam transaksi ini 
        nama_lengkap = request.form.get('nama_lengkap')
        alamat = request.form.get('alamat')
        cart_ids = request.form.getlist('id_keranjang')
        '''request.form.getlist('key'): 
        Metode ini mengembalikan daftar (list) nilai untuk kunci yang diberikan. 
        Ini berguna ketika Anda memiliki beberapa nilai dengan kunci yang sama dalam data POST. Misalnya, ketika Anda memiliki beberapa kotak centang 
        dengan nama yang sama pada formulir HTML, dan pengguna memeriksa beberapa dari mereka, Anda ingin menggunakan request.form.getlist('key') 
        untuk mendapatkan semua nilai yang dipilih oleh pengguna.

        Misalnya, dalam kasus Anda di mana Anda mengambil alamat dan cart_ids dari formulir yang dikirim dengan metode POST, 
        jika cart_ids adalah sebuah field yang mengandung beberapa nilai (misalnya, id keranjang yang dipilih pengguna), 
        Anda harus menggunakan request.form.getlist('cart_ids') agar Anda bisa mendapatkan semua nilai yang dikirim oleh pengguna.

        Jadi, penggunaan request.form.get() atau request.form.getlist() tergantung pada struktur data yang Anda harapkan dari permintaan POST Anda.
        '''
        for cart_id in cart_ids :
            cart = KERANJANG.coba_pick_id_keranjang(cart_id) #disini cart akan memiliki value id dari keranjang dari yang dimasukkan dari cart ids
            if cart is None:
                return 'eror data tidak ada di dalam keranjang'
            
            stok_keranjang = int(cart ['kuantitas']) #stok keranjang disini akan memiliki nilai int dari kuantitas keranjang yang dipilih
            produk = BARANG.pick_id_barang(cart['barang_id']) #produk disini akan memiliki value dictionary yang berisi isi semua bagan dari barang yang ada di cart
            test = produk ['id'] #mendapatkan value dari id produk
            # print(f'INI TES {test} dan ini adalah hasil dari {produk}')

            if int(produk['stok']) < (stok_keranjang) : #jika stok dalam produk kurang dari stok keranjang maka akan eror
                return f"stok dari barang dalam keranjang dengan nomor  {produk['id']} tidak mencukupi"
            
            total = produk['harga'] * cart ['kuantitas'] #mendapatkan hasil dari harga di barang dan kuantitas di keranjang

            transaksi = TRANSAKSI.coba_transaksi(nama_lengkap,alamat,user_id) #melakukan insert data ke transaksi
            TRANSAKSI_D.coba_transaksi(transaksi,test,cart['kuantitas'],total)# memasukkan insert data ke transaksi detail

            update_kuantitas_barang = produk['stok'] - stok_keranjang #update kuantitas produk barang
            # print(update_kuantitas_barang)
            BARANG.update_kuantitas(update_kuantitas_barang,produk['id']) #update stok langsung tabel barang
            if cart['id'] == 0 :
                KERANJANG.delete_keranjang(cart['id'])#menghapus keranjang ketika transaksi sudah terverivikasi semua diatas sebelum commit ke database
        #coba dulu tanpa menghapus keranjang
        koneksidatabase.commit() #commit ke database 
        return'',200
    except Exception as e :
        koneksidatabase.rollback()
        raise e
    finally:
        Connection.close() 
        

'''Note 
request.form.getlist('id_keranjang'), itu akan mengambil semua nilai yang dikirimkan dalam bentuk list. 
Kemudian, dalam loop for cart_id in cart_ids, cart_id akan berisi nilai dari setiap item dalam list cart_ids pada setiap iterasi loop.

Jadi, jika Anda memasukkan angka 3 dalam cart_ids, maka cart_ids akan menjadi list [3]. 
Selanjutnya, dalam loop for cart_id in cart_ids, cart_id akan pertama kali menjadi 3 (nilai pertama dalam list), 
dan iterasi loop akan berakhir setelah itu karena tidak ada nilai lain dalam list.

Namun, jika Anda memasukkan beberapa angka, misalnya [1, 2, 3], maka setiap nilai akan diperlakukan secara terpisah dalam setiap iterasi loop. 
Dalam kasus ini, loop akan dieksekusi tiga kali, satu untuk setiap nilai dalam list tersebut. Jadi, cart_id akan menjadi 1 pada iterasi pertama, 
2 pada iterasi kedua, dan 3 pada iterasi ketiga.
'''

