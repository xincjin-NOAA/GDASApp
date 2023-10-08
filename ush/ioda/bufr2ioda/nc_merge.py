from utils import nc_merge, timing_decorator


@timing_decorator
def main():
    esamua_names = [
        'gdas.t12z.esamua_metop-b.tm00.nc',
        'gdas.t12z.esamua_metop-c.tm00.nc',
        'gdas.t12z.esamua_n18.tm00.nc',
        'gdas.t12z.esamua_n19.tm00.nc'
    ]

    amsua_names = [
        'gdas.t12z.amsua_metop-b_ta.tm00.nc',
        'gdas.t12z.amsua_metop-c_ta.tm00.nc',
        'gdas.t12z.amsua_n18_ta.tm00.nc',
        'gdas.t12z.amsua_n19_ta.tm00.nc']

    target_names = [
        'gdas.t12z.amsua_metop-b_merge.tm00.nc',
        'gdas.t12z.amsua_metop-c_merge.tm00.nc',
        'gdas.t12z.amsua_n18_merge.tm00.nc',
        'gdas.t12z.amsua_n19_merge.tm00.nc']

    file_dir = '/scratch1/NCEPDEV/da/Xin.C.Jin/GDASApp/ush/ioda/bufr2ioda/testrun/'
    for file_name1, file_name2, target_name in zip(esamua_names, amsua_names, target_names):
        nc_merge(file_dir + file_name1, file_dir + file_name2, file_dir + target_name)


if __name__ == '__main__':
    main()
