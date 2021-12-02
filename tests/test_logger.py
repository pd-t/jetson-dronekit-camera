import os.path

from app.gpslogger import GPSLogger
from app.helper import create_directory


def test_gps_logger():
    output_directory = create_directory('/app/data/test', False)
    gps_logger = GPSLogger(output_directory=output_directory)
    gps_logger.log(
        latitude='123',
        longitude='456',
        altitude='789',
        heading='0'
    )
    assert os.path.exists(os.path.join(output_directory, 'GPSLogger.log'))
