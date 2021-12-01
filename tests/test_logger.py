import os.path

from app.gpslogger import GPSLogger


def test_gps_logger():
    gps_logger = GPSLogger(output_directory='/app/data/test')
    gps_logger.log(
        latitude='123',
        longitude='456',
        altitude='789',
        heading='0'
    )
    assert os.path.exists('/data/test/GPSLogger.log')
