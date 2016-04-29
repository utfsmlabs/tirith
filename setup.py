from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tirith',
    version='0.1.0',
    description='Monitoring software',
    long_description=long_description,
    url='https://github.com/utfsmlabs/tirith',
    author='René Mujica Moreau',
    author_email='rene.mujica.m@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',

        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
    keywords='monitoring',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['websockets'],
    entry_points={
        'console_scripts': [
            'tirs=tirith.server:main',
            'tirc=tirith.client:main',
        ],
    },
)