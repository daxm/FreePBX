#!/usr/bin/env python

from userdata import *
import os

excluded_file = os.path.join(workdir, excluded_files_filename)

if not os._exists(excluded_file):
    with open(excluded_file, 'w'):
        pass
with open('excluded_extensions', 'r') as file:
    excluded_files = file.read().splitlines()

for file in cfg_files:
    if 'MN_' in file and file not in excluded_files:
        print(file)
    else:
        print("{} is being excluded.".format(file))
