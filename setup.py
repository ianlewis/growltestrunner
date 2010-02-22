#!/usr/bin/env python

from setuptools import setup
 
setup (
    name='growltestrunner',
    version='0.1',
    description='A test runner that gives you desktop notifications',
    author='Yosuke Ikeda',
    author_email='ae35@gmail.com',
    url='http://bitbucket.org/ae35/growltestrunner/',
    license='MIT License',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Plugins',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: BSD License',
      'Topic :: Software Development :: Testing',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['growltestrunner'],
    package_data={'growltestrunner': ['*.png']},
)
