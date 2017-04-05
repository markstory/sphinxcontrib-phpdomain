# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = open('./requirements.txt', 'r')

long_desc = '''
This package contains the phpdomain Sphinx extension.

This extension provides a PHP domain for sphinx
'''

setup(
    name='sphinxcontrib-phpdomain',
    version='0.2.3',
    url='https://github.com/markstory/sphinxcontrib-phpdomain',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-phpdomain',
    license='BSD',
    author='Mark Story',
    author_email='mark@mark-story.com',
    description='Sphinx "phpdomain" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements.readlines(),
    namespace_packages=['sphinxcontrib'],
)
