""" query to insert data """

from sqlalchemy import text


def check_rows(conn, d):
    check = text("""
        SELECT
              date, uf
          FROM sii.aux_uf
         WHERE date=:date
    """)

    result = conn.execute(check, date=d)
    return result.fetchone()


def insert_rows(conn, parser):
    for d, v in parser.uf_entries.items():
        print(check_rows(conn, d))

        if check_rows(conn, d) is None:
            query = text("""
                INSERT INTO sii.aux_uf
                    (date, uf)
                VALUES
                    (:date, :value)
            """)
            print(query, d, v)

            conn.execute(query, dateexists=d, date=d, value=v)
