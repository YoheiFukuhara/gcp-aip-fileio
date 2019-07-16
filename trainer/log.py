from logging import getLogger, DEBUG, config
import json
import argparse

from tensorflow.python.lib.io import file_io


# Parameters
ARGS = None


def main():
    with file_io.FileIO(ARGS.log_config, 'r') as f:
        log_conf = json.load(f)

    # replace from INFO to DEBUG if parameter verbose is set
    if ARGS.verbose:
        log_conf["handlers"]["consoleHandler"]["level"] = DEBUG

    # read logging configuration json file
    config.dictConfig(log_conf)

    logger = getLogger(__name__)

    logger.info('Hello World! info')
    logger.debug('Hello World! debug')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-l', '--log_config',
        default='../log_config.json',
        help='Log configuration file'
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='Log level DEBUG'
    )

    ARGS, _ = parser.parse_known_args()
    main()
