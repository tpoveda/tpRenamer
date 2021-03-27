#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpDcc-tools-renamer
"""

from __future__ import print_function, division, absolute_import

import os
import sys
import logging.config


def create_logger(dev=False):
    """
    Creates logger for current tpDcc-tools-renamer package
    """

    logger_directory = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpDcc', 'logs', 'tools'))
    if not os.path.isdir(logger_directory):
        os.makedirs(logger_directory)

    logging_config = os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))

    logging.config.fileConfig(logging_config, disable_existing_loggers=False)
    logger = logging.getLogger('tpDcc-tools-renamer')
    dev = os.getenv('TPDCC_DEV', dev)
    if dev:
        logger.setLevel(logging.DEBUG)
        for handler in logger.handlers:
            handler.setLevel(logging.DEBUG)

    return logger


def register_vendors():
    """
    Adds vendors folder to sys.path (if exists)
    This vendor folder is generated by the tool build process and its necessary if we want to launch the tool
    individually
    """

    vendors_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vendors')
    if not os.path.isdir(vendors_folder) or vendors_folder in sys.path:
        return

    sys.path.append(vendors_folder)


create_logger()
register_vendors()
