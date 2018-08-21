# -*- coding: utf-8 -*-

import logging
import subprocess

from os import listdir, remove
from os.path import isfile, join, isdir
import re
from typing import List
from typing import Optional

def run_win(cmd:str=None):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # Return the output stream
    for line in process.stdout:
        result.append(line)

    # Return the error when executing the command
    if process.returncode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)

    # If no error was returned, the output is printed
    for line in result:
        logging.info(line.decode("utf-8"))


def list_directories(path:str=None)->Optional[List[str]]:
    dir_list = [f for f in listdir(path) if isdir(join(path, f))]
    if not dir_list:
        return None
    else:
        return dir_list

def list_files(path:str=None, ext:str=None)->Optional[List[str]]:
    list_files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(ext)]

    if not list_files:
        return None
    else:
        return list_files


def purge(dir:str=None, pattern:str=None)->None:
    for f in listdir(dir):
        if re.search(pattern, f):
            remove(join(dir, f))

    return None
