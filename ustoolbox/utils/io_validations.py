# -*- coding: utf-8 -*-
import os


def is_accessible(path: str, mode: str = 'r') -> bool:
    '''Check if the file at `path` can
    be accessed by the program using `mode` open flags.

    Parameters
    ----------
    path : str
        Path for the file to validate.
    mode : str

    Returns
    -------
        True, if the file exists, otherwise, False
    '''

    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


def is_empty(path: str) -> bool:
    '''Check if the file is empty

    Parameters
    ----------
    path : str
        Path for the file to validate

    Returns
    -------
        True, if the file is empty, otherwise, False
    '''
    return os.stat(path).st_size == 0


def is_base_directory(path: str) -> bool:
    ''' Check if the base directory of a file exists.

    Parameters
    ----------
    path : str
        Path to the file

    Returns
    -------
        True, if the directory exists, otherwise, False
    '''
    return os.path.exists(os.path.dirname(path))


def is_directory(path: str) -> bool:
    ''' Check if the directory exists

    Parameters
    ----------
    path : str
        Path to the file

    Returns
    -------
        True, if the directory exists, otherwise, False
    '''
    return os.path.exists(path)


def is_dir_empty(path: str) -> bool:
    ''' Check if the directory is empty

    Parameters
    ----------
    path : str
        Path to the file

    Returns
    -------
        True, if the directory is empty, otherwise, False
    '''
    if not os.listdir(path):
        return True
    else:
        return False
