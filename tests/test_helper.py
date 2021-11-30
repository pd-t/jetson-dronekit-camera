import os.path

from app.helper import create_directory


def test_create_directory():
    output_directory = '/date'
    created_directory = create_directory(output_directory=output_directory,
                                         timestamp_directory=False)
    assert output_directory == created_directory
    created_directory = create_directory(output_directory=output_directory,
                                         timestamp_directory=True)
    assert output_directory != created_directory
    assert os.path.exists(created_directory)


