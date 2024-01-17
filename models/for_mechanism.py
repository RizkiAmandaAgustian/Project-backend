from static.for_connectionDB import koneksidatabase
from flask import request 
import time
import os



#USERS


#KATEGORI
        


#BARANG



#KERANJANG



# TRANSAKSI


#TRANSAKSI DETAIL



#TES PAGINASI

def paginasi (page : int, limit : int, keyword: str = None):
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

def upload_gambar(location, id : str):
    
    connection = koneksidatabase.cursor()
    try :
        connection.execute('update barang SET image =%s where id =%s ',(location,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()
    return 'file upload sukses'

# def edit_gambar(id):
#     connection = koneksidatabase.cursor()
#     try :
#         connection.execute('SELECT id , image FROM image WHERE id = %s ',(id))
#         ambil = connection.fetchone()
#     except Exception as e :
#         koneksidatabase.rollback()
#         raise e 
#     finally : 
#         connection.close()
#         if ambil is None:
#             return 'gambar tidak tersedia'
        
#     data = {"id": ambil[0], "image": ambil[1]}

#     # Validasi file ada atau tidak
#     if "file" not in request.files:
#         return "No file part"

#     file = request.files["file"]

#     if file.filename == "":
#         return "No selected file"

#     location_new = None
#     try:
#         # Hapus file lama
#         if os.path.exists(data["image"]):
#             os.remove(data["image"])

#         # Simpan file baru
#         location_new = "static/uploads/" + str(time.time()) + "_" + file.filename
#         file.save(location_new)

#         # Update database
#         connection = koneksidatabase.cursor()
#         connection.execute("UPDATE images SET image = %s WHERE id = %s", (location_new, id))
#         koneksidatabase.commit()
#         connection.close()
#     except Exception as e:
#         if location_new is not None:
#             os.remove(location_new)
#         raise e

#     return "File edited successfully"

def pick_id_gambar(id) :
    connection = koneksidatabase.cursor()
    try: 
        connection.execute('SELECT id,image FROM image WHERE id = %s',(id,))
        gambar = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close ()
    if gambar is None :
        return None
    return {
        'id' : gambar [0],
        'image':gambar[1]
    }

def hapus_gambar(id):
    connection = koneksidatabase.cursor()
    try : 
        connection.execute('DELETE FROM image where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    return 'berhasil dihapus'