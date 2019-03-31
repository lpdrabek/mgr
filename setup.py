import codecs
from os import path

from setuptools import find_packages, setup

__version__ = '0.0.0'

BASE_DIR = path.abspath(path.dirname(__file__))


def load_requirements(f):
    with open(f, 'r') as file:
        return [line for line in file.readlines() if not line.startswith('#')]


with codecs.open(path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


install_requirements = load_requirements('requirements.txt')
tests_requirements = load_requirements('requirements.dev.txt')


setup(
    name='sweather',
    version=__version__,
    description='Simple Weather web app',
    long_description=LONG_DESCRIPTION,
    classifiers=[
        # Full list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author=u'Łukasz Drabek',
    dependency_links=[],
    author_email='lpdrabek@gmail.com',
    install_requires=install_requirements,
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=tests_requirements,
    license='GPLV2'
)
