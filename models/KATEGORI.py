from for_connectionDB import koneksidatabase

def get_all_data_kategori(page: int, limit: int, keyword: str = None, tipe_data_sort: str = 'asc', parameter_sorting: str = None):
    '''
    menentukan paginasi dan keyword apabila keryword terisi maka akan melakukan pencarian apabila kosong akan melakukan menampilkan data dengan sistem paginasi yang diatur di controller 
    '''
    connection = koneksidatabase.cursor()
    try: 
        page = (page - 1) * limit

        where = []

        if keyword is not None:
            where.append('label ilike %(keyword)s')

        whitelist_sort = ['id', 'label']
        whitelist_tipe_sort = ['asc', 'desc']

        if tipe_data_sort is not None :
            if tipe_data_sort not in whitelist_tipe_sort:
                raise ValueError('Harus dalam format asc atau desc'+','.join(whitelist_tipe_sort))
            if parameter_sorting not in whitelist_sort:
                raise ValueError('data yang dipilih tidak ada di dalam whitelist_tipe_sort'+','.join(whitelist_sort))
            where.append(f' ORDER BY {parameter_sorting} {tipe_data_sort}')

        if len(where) > 0:
            wheres = "WHERE " + "".join(where)

        query = f"""
        SELECT id, label 
        FROM kategori 
        {wheres}
        LIMIT %(limit)s 
        OFFSET %(offset)s
        """
        print(query)
        values = {"limit": limit, "offset": page}
        if keyword is not None:
            values['keyword'] = '%' + keyword + '%'
        values['tipe_data_sort'] = tipe_data_sort
        values['parameter_sorting'] = parameter_sorting

        connection.execute(query, values)
        kategorii = connection.fetchall()
        new_data = []
        for kategori in kategorii:
            data_baru = {
                'id': kategori[0],
                'label': kategori[1],
            }
            new_data.append(data_baru)
        
        koneksidatabase.commit()
    except Exception as e:
        koneksidatabase.rollback()
        raise e 
    finally: 
        connection.close()
    return new_data


def create_kategori (label :str):
    '''
    membuat eksekusi untuk memasukkan label kedalam tabel kategori
    '''
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
    '''
    mengambil kategori id
    '''
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
    '''
    menghapus kategori dengan memasukkan id yang ada 
    '''
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
    '''
    mengedit kategori dengan memasukkan id 
    '''
    connection = koneksidatabase.cursor()
    try:
        connection.execute('UPDATE kategori SET label =%s WHERE id = %s',(label,id))
        koneksidatabase.commit()
    except Exception as e :
        koneksidatabase.rollback()
        raise e 
    finally : 
        connection.close()