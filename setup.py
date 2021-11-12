#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='SisDiConPrA',
    version='0.1',
    # "python setup.py sdist" complains if any of author, author_email or url is not provided:
    #   warning: check: missing required meta-data: url
    #   warning: check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) must be
    #   supplied
    author="Grupo PI Univesp",
    author_email="xapo@xapo.com",
    url="http://www.univesp.br",
    packages=[
        'sisdiconpra',
        'sisdiconpra.api',
        'sisdiconpra.api.v1',
        'sisdiconpra.common',
        'sisdiconpra.core',
        'sisdiconpra.persistence',
        'sisdiconpra.services',
        'sisdiconpra.webapp'
    ],

    # include non-Python files
    include_package_data=True,
    zip_safe=False,  # required when including non-Python files

    install_requires=[
        # 3rd Party
        "Flask==0.11.1",
        "MySQL-python==1.2.5",
        "SQLAlchemy==1.1.9",
        "colander==1.3.2",
        "oauth2client==4.0.0",
        "requests==2.13.0",
        "mysqlclient==2.0.3",
        "pymysql==1.0.2"
    ],
)
