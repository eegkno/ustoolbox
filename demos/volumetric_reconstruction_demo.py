# -*- coding: utf-8 -*-
import logging
from os import remove
from os.path import join
from ustoolbox.images.volumetric_reconstruction import crop_sequence_cmd, generate_volume_cmd
from ustoolbox.utils.command import run_win, list_directories, list_files, purge
from ustoolbox.utils.logs import set_logger

if __name__ == '__main__':

    set_logger(1)

    base_dir = 'D:/US/'
    config_file = 'C:/Users/Edgar/Desktop/us_acquisition/VolumeReconstructor.xml'

    # Get all the sub-directories in base_dir
    dir_l = list_directories(base_dir)

    # Walk all the sub-directories
    for dir in dir_l:
        user_dir = join(base_dir, dir)

        # Clean previous files
        purge(user_dir, 'CROP')
        purge(user_dir, 'VOLUME')

        # Get the list of .mha files
        files_user =  list_files(user_dir, '.mha')
        logging.info('Subject: {}'.format(dir))

        # Crop ROI and generate volumes
        for file in files_user:
            to_process = join(user_dir, file)
            logging.info('File being processed: {}'.format(to_process))
            cmd_1, cmd_2, crop2= crop_sequence_cmd(to_process)
            logging.info(cmd_1)
            logging.info(cmd_2)
            run_win(cmd_1)
            run_win(cmd_2)
            cmd = generate_volume_cmd(config_file, crop2)
            logging.info(cmd)
            run_win(cmd)
