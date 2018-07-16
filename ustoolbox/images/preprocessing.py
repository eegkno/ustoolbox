# -*- coding: utf-8 -*-

# import the necessary packages
import cv2
import logging
import os
import numpy as np
from os.path import splitext
from imutils import paths

from ustoolbox.utils.io_validations import (is_dir_empty, is_directory, is_accessible)


# Reference frame
# 0/0---X--->
#  |
#  |
#  Y
#  |
#  |
#  v

def crop_roi_dir(input_path: str, output_path: str) -> None:
    '''
        Crop all the images in a specified directory

    Parameters
    ----------
    input_path :str
        Path to the directory that contains the original files
    output_path :str
        Path to the directory to store the cropped images

    Returns
    -------
        None
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
        crop_roi_image(image_path, output_path)

    logging.info('Done!')


def crop_roi_image(image_path: str, output_path: str = None) -> None:
    '''
        Crop an image in a roi

    Parameters
    ----------
    image_path : str
        Path of the original image
    output_path : str
        Path to save the cropped image

    Returns
    -------
        None
    '''

    if not is_accessible(image_path):
        raise ValueError('The {} does not exists'.format(image_path))

    # If not directory specified
    if output_path == None:
        output_path = './'
    else:
        if not is_directory(output_path):
            logging.info("Output directory {} does not exist, creating directory".format(output_path))
            try:
                os.makedirs(output_path)
            except OSError:
                print('Error: Creating directory {} '.format(output_path))

    logging.debug('Original image: {}'.format(image_path))
    _, full_filename = os.path.split(image_path)
    file_name, extension = splitext(full_filename)

    cropped = crop_roi(image_path)

    new_name = '{}_crop{}'.format(file_name, extension)

    # write the cropped image to disk
    cropped_path = os.path.join(output_path, new_name)

    if is_accessible(cropped_path):
        raise ValueError('There is a file with the name {} in the dir {}'.format(new_name, output_path))
    else:
        cv2.imwrite(cropped_path, cropped)
        logging.debug('Cropped image: {}'.format(cropped_path))


def crop_roi(image_path: str) -> np.array:
    '''
        Crop a fixed section of an image

    Parameters
    ----------
    image_path : str
        Path of the image to be cropped.

    Returns
    -------
        np.array that contains the cropped image.
    '''

    # read images
    image = cv2.imread(image_path, 0)

    # image(0:cY, 0:cX)
    cropped = image[40:435, 166:366]

    return cropped
