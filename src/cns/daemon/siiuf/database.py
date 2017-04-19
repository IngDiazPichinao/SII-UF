""" Setup database """

from sqlalchemy import create_engine


def connect(args):
    engine = create_engine(
        'postgresql+psycopg2://{user}:{passwd}@{host}/{database}'
        .format(
            user     = args['--user'],
            passwd   = args['--passwd'],
            host     = args['--host'],
            database = args['--database']
        )
    )

    return engine
