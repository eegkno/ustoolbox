# -*- coding: utf-8 -*-

from ustoolbox.images.capture import capture_sequence
from ustoolbox.utils.logs import set_logger

if __name__ == '__main__':

    set_logger(1)
    output_dir = 'dataset/test_sequence_a'
    capture_sequence(output_dir, everyFrame = 3)
