""" Loggin setup

Level values memo:
CRITICAL 50
ERROR    40
WARNING  30
INFO     20
DEBUG    10
NOSET    0
"""

import logging
import sys

from systemd import journal
from logging import StreamHandler

log = logging.getLogger()


def setup_logging(args):
    if (args['--debug']):
        stream_handler = StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        logging.root.addHandler(stream_handler)

        handler = journal.JournalHandler(SYSLOG_IDENTIFIER='cns-daemon-siiuf')
        handler.setLevel(logging.DEBUG)
        logging.root.addHandler(handler)
