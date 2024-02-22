from for_connectionDB import koneksidatabase
from flask import request
import os,time

def upload_gambar(location):
    
    connection = koneksidatabase.cursor()
    try :
        connection.execute('INSERT INTO image (image) values (%s)',(location,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()
    return 'file upload sukses'

def edit_gambar(id):
    connection = koneksidatabase.cursor()
    ambil = None
    try :
        connection.execute('SELECT id , image FROM image WHERE id = %s ',(id,))
        ambil = connection.fetchone()
        
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()
    
    if ambil is None:
            return 'gambar tidak tersedia'
        
        
    data = {"id": ambil[0], "image": ambil[1]}

    # Validasi file ada atau tidak
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    location_new = None
    try:
        # Hapus file lama
        if os.path.exists(data["image"]):
            os.remove(data["image"])

        # Simpan file baru
        location_new = "static/uploads/" + str(time.time()) + "_" + file.filename
        file.save(location_new)

        # Update database
        connection = koneksidatabase.cursor()
        connection.execute("UPDATE image SET image = %s WHERE id = %s", (location_new, id))
        koneksidatabase.commit()
        connection.close()
    except Exception as e:
        if location_new is not None:
            os.remove(location_new)
        raise e

    return "File edited successfully"

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
        gambar = pick_id_gambar(id)
        connection.execute('DELETE FROM image where id = %s',(id,))
        koneksidatabase.commit()
        if os.path.exists(gambar["image"]):
            os.remove(gambar["image"])

    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    return 'berhasil dihapus'