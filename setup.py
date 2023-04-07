#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='chessmovv',
    version='0.0.4',
    description='Valida si el movimiento de una pieza en ajedrez es válido',
    packages=find_packages(),
    
    author='Andrés D. Pérez',
    author_email='andapzz@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='ajedrez reina movimiento validar',
)