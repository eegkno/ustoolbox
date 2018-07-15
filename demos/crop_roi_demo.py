# -*- coding: utf-8 -*-

from ustoolbox.utils.logs import set_logger
from ustoolbox.images.preprocessing import crop_roi

if __name__ == '__main__':


    set_logger(1)
    input_dir = 'dataset/test_crop_input'
    output_dir = 'dataset/test_crop_output'
    crop_roi(input_dir, output_dir)
