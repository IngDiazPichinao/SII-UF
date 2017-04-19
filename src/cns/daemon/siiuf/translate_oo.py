""" Get data information from sii to get value UF.
"""
import re
import datetime

from lxml import html

import requests
import locale


NOW = datetime.datetime.now()


class UFParser:

    def __init__(self):
        self._url_base = "http://www.sii.cl/pagina/valores/uf/uf"
        self._url_year = NOW.year
        self._url      = self._url_base + str(self._url_year) + ".htm"
        self._page     = requests.get(self._url)
        self._tree     = html.fromstring(self._page.content)

        self._entries = {}

    @property
    def uf_entries(self):
        if not self._entries:
            rows   = self._tree.xpath('//*/table[@class="tabla"]/tbody/tr')
            by_day = [tr.xpath('*/text()') for tr in rows]

            for dayrow in by_day:
                assert dayrow,                           "Expected days in the dayrow"
                assert re.match("^\d{1,2}$", dayrow[0]), "First entry in daily row must be the day"
                day = int(dayrow[0])

                for idx, day_value in enumerate(dayrow[1:]):
                    if day_value == "\xa0":
                        value = 0
                    else:
                        assert re.match("^\d{2}\.\d{3}\,\d{2}", day_value), "Could not make out UF value"

                        value = locale.atof(day_value)
                        month = idx + 1
                        date  = datetime.date(year=NOW.year, month=month, day=day)

                    self._entries[date] = value

        return self._entries

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "es_CL.UTF-8")

    parser = UFParser()
    for date, uf in parser.uf_entries.items():
        print(date, uf)
