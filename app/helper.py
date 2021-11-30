import os
from time import sleep
from datetime import datetime


def create_directory(output_directory: str,
                     timestamp_directory: bool = True):
    if timestamp_directory:
        timestamp = datetime.today().strftime("%Y%m%d%H%M%S")
        output_directory = os.path.join(output_directory, timestamp)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    return output_directory
