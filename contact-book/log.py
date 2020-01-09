# https://stackoverflow.com/a/4723380
import logging

LOGGER_FILE = 'debug.log'
LOGGER_NAME = 'contact-book'

log = logging.getLogger(LOGGER_NAME)
log.setLevel(logging.DEBUG)

# Alternative formatting available on python 3.2+:
formatter = logging.Formatter(
    "{asctime} {threadName:>11} {levelname} {message}", style='{')
c_format = logging.Formatter(
    '{name} - {levelname} - {message}', style='{')
f_format = logging.Formatter(
    '{asctime} - {name} - {levelname} - {message}', style='{')

# Log to file
file_handler = logging.FileHandler(LOGGER_FILE, "w")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(f_format)
log.addHandler(file_handler)

# Log to stdout too
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(c_format)
log.addHandler(stream_handler)

def test():
    log.debug("Some message")
    log.error("An error!")
    try:
        something()
    except:
        log.exception("An exception occured!")
    
if __name__ == "__main__":
    test()