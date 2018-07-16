# -*- coding: utf-8 -*-

from ustoolbox.utils.logs import set_logger
from ustoolbox.images.preprocessing import (crop_roi_image, crop_roi_dir)

if __name__ == '__main__':


    set_logger(1)

    # Process an image, and the output is saved in the current dir
    input_image = 'dataset/test_crop_input/IMG0000.bmp'
    crop_roi_image(input_image)

    # Process an image, and the output is saved in the current output_dir
    input_image = 'dataset/test_crop_input/IMG0000.bmp'
    output_dir = 'dataset/test_crop_output_a'
    crop_roi_image(input_image, output_dir)

    # Process a directory with images, and the output is saved in the current output_dir
    input_dir = 'dataset/test_crop_input'
    output_dir = 'dataset/test_crop_output_b'
    crop_roi_dir(input_dir, output_dir)
