import os

# workdir = '/tftpboot/mitel_patch'
workdir = '.'
#cfg_file_dir = '/tftpboot'
cfg_file_dir = './samplefiles'

excluded_files_filename = 'excluded_extensions'
cfg_files = os.listdir(cfg_file_dir)
