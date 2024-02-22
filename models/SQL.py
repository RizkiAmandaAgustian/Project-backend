from for_connectionDB import koneksidatabase
from models.KATEGORI import pick_id_kategori

def get_allAAAAA():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id, nama_barang, deskripsi, harga, stok, kategori_id from barang')
        items = []
        for item in connection.fetchall():
              category = None
              if item[5] is not None:
                  category = pick_id_kategori(item[5])
  
              items.append(
                  {
                      "id": item[0],
                      "nama_barang": item[1],
                      "deskripsi": item[2],
                      "harga": item[3],
                      "stok": item[4],
                      "kategori_id": item[5],
                      "category": category,
                  }
              )
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback() 
        raise e
    finally:
        connection.close()
        return items

def sqlljoin():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('select b.nama_barang, b.deskripsi, b.stok , td.kuantitas, td.harga from barang b  join transaksi_detail td on b.id = td.barang_id')
        koneksidatabase.commit()
        item = connection.fetchall()
        if item is None:
            return None
        items = []
        for todo in item:
            new_todo = {
        'nama_barang' : todo [0],
        'deskripsi' : todo [1],
        'stok' : todo [2],
        'kuantitas' : todo [3],
        'harga' : todo [4]
    
            }
            items.append(new_todo)
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    return items