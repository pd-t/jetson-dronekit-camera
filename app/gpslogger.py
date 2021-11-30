import os
import logging


class GPSLogger:
    def __init__(self,
                 output_directory: str):
        self.logger = self.__create_logger(output_directory)

    @staticmethod
    def __create_logger(output_directory: str):
        logger = logging.getLogger('GPSLogger')
        logger.setLevel(logging.INFO)
        log_filename = os.path.join(output_directory, 'GPSLogger.log')
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.INFO)
        logger.addHandler(fh)
        formatter = logging.Formatter('%(asctime)s;'
                                      '%(name)s;'
                                      '%(levelname)s;'
                                      '%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def log(self,
            latitude: str,
            longitude: str,
            altitude: str,
            heading: str
            ):
        msg = ';'.join([latitude, longitude, altitude, heading])
        self.logger.info(msg)
