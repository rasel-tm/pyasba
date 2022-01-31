import shutil
from google_drive_downloader import GoogleDriveDownloader as gdd

def make_zip(output_filename, dir_name):
    shutil.make_archive(output_filename, 'zip', dir_name)
    print(f'Successfully created {output_filename}.zip file from {dir_name}!')

def make_unzip(input_file, output_dir):
    shutil.unpack_archive(input_file, output_dir, 'zip')
    print(f'Successfully Unzipped {input_file}.zip file saved to {input_file}!')


gdd.download_file_from_google_drive(file_id='1ZBKxnMF0bxOiqxTWRahbvubdgun9wQUS',
                                    dest_path='./datasets.zip',
                                    unzip=True, showsize=True)