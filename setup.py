import os
from setuptools import setup, find_packages

setup(
    name='shallow-water-solver',
    version='1.0.0',
    license='MIT',
    description='Solver for 2D Shallow Water Equations',
    author='Abdol Mehdi Behroozi',
    author_email='behroozi.fx.com',
    url='https://github.com/AMBehroozi/shallow-water-solver',
    packages=find_packages(exclude=['*.tests']),
    package_data={'': ['*.txt', '*.npz']},
    long_description='A solver for 2D shallow water equations.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=['numpy', 'h5py'],
)
