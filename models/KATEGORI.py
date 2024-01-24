from static.for_connectionDB import koneksidatabase

def get_all_data_kategori (page : int, limit : int, keyword: str = None):
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1 ) * limit

        whereKeyword = ""

        if keyword is not None:
            whereKeyword = " WHERE label ilike %(keyword)s "

        query = f"""
        SELECT id,label 
        FROM kategori 

        {whereKeyword}

        limit %(limit)s 
        offset %(offset)s

        """
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = '%'+keyword+'%'

        connection.execute(query,values)
        kategorii = connection.fetchall()
        new_data = []
        for kategori in kategorii :
            data_baru = {
                'id' : kategori [0],
                'label': kategori [1],
            }
            new_data.append(data_baru)
        
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally: 
        connection.close()
    return new_data

def create_kategori (label :str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('INSERT INTO kategori (label) VALUES (%s)',(label,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally:
        connection.close()

def pick_id_kategori (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('SELECT id,label from kategori where id = %s',(id,))
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
        'id': laptop [0],
        'label' : laptop [1],
    }

def delete_kategori (id):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('DELETE from kategori where id = %s',(id,))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally :
        connection.close()

def edit_kategori (id,label : str):
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE kategori SET label =%s WHERE id = %s',(label,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()