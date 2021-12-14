import datetime
import inspect
import logging

import allure


def customLogger():
    logName = inspect.stack()[1][3]

    logger = logging.getLogger(logName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("../reports/{0}.log".format(datetime.datetime.now()), mode='a')

    fileHandler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %H:%M:%S')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
