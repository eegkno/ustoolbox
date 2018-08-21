# -*- coding: utf-8 -*-

from os.path import join, split, splitext
from typing import Tuple

from ustoolbox.utils.command import run_win

def crop_sequence_cmd(file:str=None)-> Tuple[str, str, str]:
    cmd_1 = 'C:/Users/Edgar/PlusApp-2.6.0.20180120-Win32/bin/EditSequenceFile.exe --operation=CROP'
    cmd_2 = 'C:/Users/Edgar/PlusApp-2.6.0.20180120-Win32/bin/EditSequenceFile.exe --operation=CROP'

    roi_1 = ' --rect-origin 217 70  --rect-size 400 361'
    roi_2 = ' --rect-origin 0 20  --rect-size 182 292'

    input = '--source-seq-file={}'.format(file)
    #print(input)

    base_name, full_filename = split(file)
    file_name, extension = splitext(full_filename)


    crop_1 = '{}_CROP1{}'.format(join(base_name, file_name), extension)
    crop_2 = '{}_CROP2{}'.format(join(base_name, file_name), extension)


    output_1 = '--output-seq-file={}'.format(crop_1)
    output_2 = '--output-seq-file={}'.format(crop_2)

    cmd_1 = '{} {} {} {}'.format(cmd_1, roi_1, input, output_1)
    cmd_2 = '{} {} {} {}'.format(cmd_2, roi_2, output_1.replace('output', 'source'), output_2)

    return cmd_1, cmd_2, crop_2

def generate_volume_cmd(config_file:str=None, source_file:str=None)->str:

    cmd = 'C:/Users/Edgar/PlusApp-2.6.0.20180120-Win32/bin/VolumeReconstructor.exe'
    output = source_file.replace('CROP2', 'VOLUME')
    cmd = '{} --config-file={} --source-seq-file={} --output-volume-file={} --image-to-reference-transform=ImageToReference'.format(cmd, config_file, source_file, output)

    return cmd
