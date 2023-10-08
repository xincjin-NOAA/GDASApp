import argparse
from bufr2ioda_base import Bufr2IodaBase
#from wxflow import Logger
from logging import Logger


logger = Logger('BUFR2IODA_satwind_amv_goes.py', level='DEBUG')


class Bufr2IodaAmusa(Bufr2IodaBase):
    pass


class Bufr2IodaEbmua(Bufr2IodaBase):

    def re_map_variable(self, data):
        #  TODO replace this follow that in GSI
        # read_bufrtovs.f90
        # antcorr_application.f90
        # search the keyword “ta2tb” for details

        sat_ids = data.allSubCategories()
        for sat_id in sat_ids:
            td = data.get('variables/antennaTemperature', sat_id)
            ifov = data.get('variables/fieldOfViewNumber', sat_id)
            tb = self.apply_ant_corr(td,ifov)
            data.set('variables/antennaTemperature', tb, sat_id)  # TODO to set dim path in cpp

    def apply_ant_corr(self, td, ifov):
        # TODO replace real function
        tb = td * 1.4
        return tb


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--type', type=str, help='Input Satellite type a/e', required=True)
    parser.add_argument('-c', '--config', type=str, help='Input JSON configuration', required=True)
    parser.add_argument('-v', '--verbose', help='print debug logging information',
                        action='store_true')
    args = parser.parse_args()
    log_level = 'DEBUG' if args.verbose else 'INFO'
    logger = Logger('BUFR2IODA_satwind_amv_goes.py', level=log_level)
    if args.type == 'a':
        convert = Bufr2IodaAmusa(args.config)
    elif args.type == 'e':
        convert = Bufr2IodaEbmua(args.config)
    else:
        exit()
    convert.execute()
    amsua_files = convert.split_files
    print(amsua_files)
    logger.info('Converting amsua done!')
