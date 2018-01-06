#!/usr/bin/env python

import os

workdir = '.'
excluded_file = os.path.join(workdir, 'excluded_extensions')

cfg_files = os.listdir('./samplefiles')

excluded_files = []
if not os._exists('excluded_extensions'):
    with open()
with open('excluded_extensions', 'r') as file:
    excluded_files = file.read().splitlines()

for file in cfg_files:
    if 'MN_' in file and file not in excluded_files:
        print(file)
    else:
        print("{} is being excluded.".format(file))
