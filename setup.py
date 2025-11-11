from setuptools import setup

with open("README.MD", "r", encoding="utf-8") as f:
    long_description = f.read()

AUTHOR_NAME = 'SALIM KHA'
SRC_REPO = 'SRC'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
name = SRC_REPO,
version = '0.0.1',
author = AUTHOR_NAME,
author_email ="salimkha281@gmailcom",
decription = 'A small example package for movies recommendation',
long_description= long_description,
long_description_content_type = 'text/markdown',
package = [SRC_REPO],
python_requires = '> 3.13.5',
install_requires = LIST_OF_REQUIREMENTS
,
)
