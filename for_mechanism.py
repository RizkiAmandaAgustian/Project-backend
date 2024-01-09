from for_connectionDB import koneksidatabase

def get_all_data ():
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT no,seri_laptop,support_thunderbolt FROM data_barang')
        result = connection.fetchall()
        new_data = []
        for serilaptop in result :
            data_baru = {
                'no' : serilaptop [0],
                'seri_laptop': serilaptop [1],
                'support_thunderbolt': serilaptop [2],
            }
            new_data.append(data_baru)
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        koneksidatabase.close()
    return new_data

def create (seri_laptop : str , support_thunderbolt : bool):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO data_barang (seri_laptop,support_thunderbolt) VALUES (%s,%s)',(seri_laptop,support_thunderbolt))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id (no):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT no,seri_laptop,support_thunderbolt from data_barang where no = %s',(no,))
        laptop = connection.fetchone()
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()
    if laptop is None:
        return None
    return{
        'no': laptop [0],
        'seri_laptop' : laptop [1],
        'support_thunderbolt': laptop [2]
    }