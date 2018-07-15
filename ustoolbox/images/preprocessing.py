# -*- coding: utf-8 -*-

# import the necessary packages
import logging
import os
import time

import cv2
import numpy as np
from imutils import paths
from threading import Thread
from queue import Queue

from ustoolbox.utils.io_validations import (is_dir_empty, is_directory)

# Reference frame
# 0/0---X--->
#  |
#  |
#  Y
#  |
#  |
#  v

def crop_roi(input_path: str, output_path: str) -> None:
    '''
        Crop US images with a fix window

    Parameters
    ----------
    input_path :str
        Path to the directory that contains the original files
    output_path :str
        Path to the directory to store the cropped images

    Returns
    -------

    '''

    # Validation of parameters
    if not is_directory(input_path):
        raise ValueError('The input directory does not exist')

    if is_directory(output_path):
        logging.info("Ouput directory {} already exists".format(output_path))
        if not is_dir_empty(output_path):
            raise ValueError('The output directory is not empty')

    else:
        logging.info("Output directory {} does not exist, creating directory".format(output_path))
        try:
            os.makedirs(output_path)
        except OSError:
            print('Error: Creating directory {} '.format(output_path))

    logging.info('Processing directory: {}'.format(output_path))

    for image_path in sorted(list(paths.list_images(input_path))):
        logging.debug('Original image: {}'.format(image_path))
        _, filename = os.path.split(image_path)

        # read images
        image = cv2.imread(image_path, 0)

        # image(0:cY, 0:cX)
        cropped = image[40:435, 166:366]

        # write the cropped image to disk
        cropped_path = os.path.join(output_path, filename)
        cv2.imwrite(cropped_path, cropped)
        logging.debug('Cropped image: {}'.format(cropped_path))

    logging.info('Done!')











