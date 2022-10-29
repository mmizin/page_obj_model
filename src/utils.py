from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import functools


def wait_presence_of_element_located(func):
    def wrapper(*args, **kwargs):
        wait_time = 8
        func(*args, *kwargs)
        custom_wait = WebDriverWait(kwargs['driver'], wait_time)
        custom_wait.until(EC.element_to_be_clickable(kwargs['selector']))

    return wrapper


def retry(tries=3, wait=1, backoff=2, error_message=None):
    def retry_wrapper(func):
        @functools.wraps(func)
        def sub_wrapper(*args, **kwargs):
            _tries, _wait = tries, wait
            while _tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    _tries -= 1
                    _wait *= backoff
                    print(f'Exception: {e}.\nFunction: {func.__name__}.\n Error message: {error_message}.\n '
                          f'Retries left {tries}.')

                    sleep(_wait)

                    if not _tries:
                        raise SystemExit(f'No tries left!\n '
                                         f'Exception: {e}.\n '
                                         f'Function: {func.__name__}.\n '
                                         f'Error message: {error_message}.\n')
        return sub_wrapper
    return retry_wrapper
