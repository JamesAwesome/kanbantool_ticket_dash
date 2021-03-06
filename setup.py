from setuptools import setup

setup(
    name='kanbantool_ticket_dash',
    version='0.0.1',
    packages=[
        ''
    ],
    package_dir={'': 'kanbantool_ticket_dash'},
    install_requires=[
        'arrow >=0.10,<0.14',
        'Flask >=0.12.2,<1.1',
        'Flask-Script >= 2.0.5, < 2.1',
        'Flask-WTF >= 0.14.2, < 0.15',
        'requests >=2.14.2,<2.22',
        'gunicorn >=19.7.1,<19.10',
        'slackclient >=1.0.5,<1.4',
    ]
)
