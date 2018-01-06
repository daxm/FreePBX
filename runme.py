#!/usr/bin/env python

from userdata import *
import os
import subprocess


def main():
    excluded_file = os.path.join(workdir, excluded_files_filename)

    if not os.path.isfile(excluded_file):
        with open(excluded_file, 'w'):
            pass
    with open('excluded_extensions', 'r') as file:
        excluded_files = file.read().splitlines()

    for file in cfg_files:
        if 'MN_' in file and file not in excluded_files:
            print("{} is being modified to fix Mitel model type in the XML.".format(file))
            true_file = os.path.join(cfg_file_dir, file)
            subprocess.call(["""sed -i -e 's/Model="5235"/Model="daxm"/g' {}""".format(true_file)], shell=True)
        else:
            print("{} is being excluded.".format(file))


if __name__ == "__main__":
    main()
