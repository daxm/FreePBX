#!/usr/bin/env python2

import os
import subprocess
import time
import logging


def main():
    logging.basicConfig(level='DEBUG')
    
    while True:
        sleep_time = 300

        workdir = '/tftpboot/mitel_patch'
        # workdir = '/home/daxm/PycharmProjects/FreePBX'

        cfg_file_dir = '/tftpboot'
        # cfg_file_dir = os.path.join(workdir, 'samplefiles')
        cfg_files = os.listdir(cfg_file_dir)

        excluded_files_filename = 'excluded_extensions'
        excluded_file = os.path.join(workdir, excluded_files_filename)

        if not os.path.isfile(excluded_file):
            with open(excluded_file, 'w'):
                pass
        with open(excluded_file, 'r') as the_file:
            excluded_files = the_file.read().splitlines()

        for the_file in cfg_files:
            if 'MN_' in the_file and the_file not in excluded_files:
                logging.info("{} is being modified to fix Mitel model type in the XML.".format(the_file))
                true_file = os.path.join(cfg_file_dir, the_file)
                subprocess.call(["""sed -i -e 's/Model="5224"/Model="5235"/g' {}""".format(true_file)], shell=True)
            else:
                logging.info("{} is being excluded.".format(the_file))
        logging.info("Sleeping for {} seconds.".format(sleep_time))
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
