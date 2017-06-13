#!/usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'python data mining scraping'

setup(name='emery',
    version='0.0.2.py3',
    description="""scraping/mining tools""",
    author='starenka',
    packages=find_packages(),
    download_url = "https://github.com/hardkun/emery",
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=['requests',
                      'pyquery',
                      'tablib',
                      'beautifulsoup4',
                      'html5tidy',
                      'pandas',
                      ],
    zip_safe=False,
    include_package_data=True,
)
