# -*- coding: utf-8 -*-
import logging


def set_logger(verbose):
    """Configure logger to use it as verbose mode in functions

    Parameters
    ----------
        verbose : int
            Level of the logger.

    Examples
    --------
        >>> import logging
        >>> from src.utils.logs import set_logger
        >>> def dummy_function(verbose=1):
        >>>     if verbose > 0:
        >>>         set_logger(verbose)
    """

    level = 0
    if verbose == 1:
        level = logging.INFO
    elif verbose == 2:
        level = logging.DEBUG
    elif verbose == 3:
        level = logging.WARNING
    elif verbose == 4:
        level = logging.ERROR
    elif verbose == 5:
        level = logging.CRITICAL

    format = '%(module)s::%(funcName)s() - %(levelname)s: %(message)s'
    datefmt = '%m-%d %H:%M'
    logging.basicConfig(level=level, format=format, datefmt=datefmt)
