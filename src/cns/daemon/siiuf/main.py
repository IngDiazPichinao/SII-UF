""" Storage values UF from SII in db

Usage:
    cns-daemon-siiuf --config <path>
                     --user <user> --passwd <passwd> --host <host> --database <database> [--port <port>]
                     [--logfile <filepath>]
                     [--debug]

Options:
    --help                      # Show this Help Message

    -c --config <path>          # Path to configuration file [default: /etc/cns/cns-daemon-sav.yml]

    -u --user <user>            # Current User
    -p --passwd <passwd>        # Current Pwd
    -h --host <host>            # Current host
    -d --db_database <dbname>   # Current DB Database Name
    -p --port <port>            # Current Port

    --logfile <filepath>        # File to log to [default: /var/log/cns/cns-daemon-siiuf.log]
    --debug                     # Output debugging information into log and stdout
"""

from docopt import docopt

from .logging      import setup_logging, log
from .translate_oo import UFParser
from .database     import connect
from .query        import insert_rows

import locale


def main():
    args = docopt(__doc__, help=True)

    locale.setlocale(locale.LC_ALL, "es_CL.UTF-8")

    setup_logging(args)

    try:
        log.info("DB Connect")
        cns = connect(args)

        parser = UFParser()

        log.info("Insert File")
        insert_rows(cns, parser)

    except:
        log.exception('Uncaught critical exception')

if __name__ == '__main__':
    main()
