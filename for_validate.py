def validation (seri_laptop,support_thunderbolt):
    error = []
    if seri_laptop is None :
        error.append('masukkan seri laptop')
    if support_thunderbolt is None :
        error.append('Masukkan apakah laptop seri ini support thunderbolt atau tidak')
    else:
        if support_thunderbolt not in ['0','1']:
            error.append('masukkan 0 atau 1 sebagai penanda apakah laptop tersebut support thunderbolt atau tidak')
    if len (error)> 0 :
        return {'error':error}