#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

requires = [
    'Django<1.9',
    'dj-database-url>=0.3.0',
    'django-braces>=1.4.0',
    '# django-configurations 0.8 does not work with Django 1.8. A fork has been',
    '# added to requirements/forks.txt that supports Django 1.8.',
    '# django-configurations==0.8',
    'django-cors-headers>=1.1.0',
    'django-countries==3.4.1',
    'django-crispy-forms>=1.4.0',
    'django-grappelli>=2.6.3',
    '# With Django>=1.9.0 we can remove django-pgjson because JSONField would be in the core:',
    '# https://docs.djangoproject.com/en/1.9/ref/contrib/postgres/fields/#jsonfield',
    'django-pgjson==0.3.1',
    'djangorestframework==3.1.1',
    'envdir>=0.7',
    'psycopg2>=2.5.4',
    'pytz>=2014.10',
]

docs_requires = [
    'Sphinx==1.2.2',
]

tests_requires = [
    'coverage==4.0.0',
    'fake-factory==0.5.3',
    'freezegun==0.2.8',
    'httpretty>=0.8.0,!=0.8.1,!=0.8.2,!=0.8.3,!=0.8.7,!=0.8.8,!=0.8.9,!=0.8.10',
    'isort==3.9.5',
    'pytest-django==2.7.0',
    'pytest-httpretty==0.2.0',
    'pytest-pythonpath==0.6',
    'pytest==2.6.4',
    'tox==1.9.2',
]

setup(
    name='hopper',
    version='0.1.0',
    description='A RESTful HTTP API for managing HTML forms.',
    long_description=read('README.rst'),
    author='reelport GmbH',
    author_email='development@picturepipe.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'docs': docs_requires,
        'tests': tests_requires,
    },
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
