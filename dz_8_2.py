from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        log.setLevel(level)
        logmsg = message if message else func.__name__
        ch = logging.StreamHandler()

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        log.addHandler(ch)

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return (func(*args, **kwargs))

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


add(1, 2)