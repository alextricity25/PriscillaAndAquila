import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PriscillaAndAquila",
    version = "0.0.1a3",
    author = "Miguel Alex Cantu",
    author_email = "miguel.can2@gmail.com",
    description = ("A command line tool that performs a lookup of Bible verse"
                   " references that can be fed in through various input"
                   " means."),
    license = "GNU General Public License v3 or later (GPLv3+)",
    keywords = "Study Bible, Memorize Bible, Holy Scriptures",
    packages=[
        'priscillaandaquila',
    ],
    install_requires = ['diyr'],
    long_description=read('README.rst'),
    url = 'https://github.com/alextricity25/PriscillaAndAquila',
    download_url = 'https://github.com/alextricity25/PriscillaAndAquila/archive/0.0.1a3.tar.gz',
    entry_points = {
        'console_scripts': [
            'priscilla = priscillaandaquila.main:main',
            'aquila = priscillaandaquila.main:main'
        ]
    }
    
)
