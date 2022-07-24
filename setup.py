from os import path
from setuptools import setup, find_packages


import miqpartners


here = path.abspath(path.dirname(__file__))

with open('README.md', 'r') as desc:
    long_description = desc.read()


setup(
    name='miqpartners',
    version=miqpartners.__version__,
    description='MTN Mobile Money API wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/marqetintl/miqpartnerspy',
    author=miqpartners.__author__,
    author_email=miqpartners.__email__,
    keywords='Ambassador program',
    packages=find_packages(),
    install_requires=['requests', 'miq'],
    extras_require={
        "dev": [
            'coverage', 'selenium',
            'pytest', 'pytest-cov', 'pytest-django',
        ]
    },
    python_requires=">=3.5",
    zip_safe=False
)
