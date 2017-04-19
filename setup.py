""" CNS SII-UF Worker daemon """


from setuptools import setup, find_packages


cfg = {
    'name'             : 'cns-daemon-siiuf',
    'long_description' : __doc__,
    'version'          : '0.1.0.dev201607120',
    'packages'         : find_packages('src'),
    'package_dir'      : {'' : 'src'},

    'namespace_packages' : [
        'cns',
        'cns.daemon'
    ],

    'install_requires' : [
        'sqlalchemy >= 0.9.8',
        'psycopg2   >= 2.6.1',
        'docopt     >= 0.6.2',
        'lxml       >= 3.4.0',
        'requests   >= 2.10.0',
        'cns-orm    >= 0.1.0.dev2015083100'
    ],

    'dependency_links' : [],
    'entry_points'     : {
        'console_scripts' : [
            'cns-daemon-siiuf = cns.daemon.siiuf.main:main'
        ]
    },

    'zip_safe' : False
}

if __name__ == '__main__':
    setup(**cfg)
