import os

# workdir = '/tftpboot/mitel_patch'
workdir = '.'
excluded_files_filename = 'excluded_extensions'
log_file = os.path.join(workdir, 'output.log')
cfg_files = os.listdir('./samplefiles')
