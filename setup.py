#!/usr/bin/env python

from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(name='pomdp-py',
      packages=['pomdp_py', 'pomdp_problems'],
      version='1.2',
      description='Python POMDP Library.',
      install_requires=[
          'numpy',
          'scipy',
          'matplotlib',
          'opencv-python',  # for some tests
          'networkx',
      ],
      author='Kaiyu Zheng',
      author_email='kaiyutony@gmail.com',
      keywords = ['Partially Observable Markov Decision Process', 'POMDP'],
      ext_modules=cythonize(['pomdp_py/algorithms/po_rollout.pyx',
                             'pomdp_py/algorithms/po_uct.pyx',
                             'pomdp_py/algorithms/pomcp.pyx',
                             'pomdp_py/algorithms/value_iteration.pyx',
                             'pomdp_py/framework/oopomdp.pyx',
                             'pomdp_py/framework/planner.pyx',
                             'pomdp_py/framework/basics.pyx',
                             'pomdp_py/representations/distribution/particles.pyx',
                             'pomdp_py/representations/distribution/histogram.pyx',
                             'pomdp_py/representations/distribution/gaussian.pyx',
                             'pomdp_py/representations/belief/particles.pyx'],
                            build_dir="build", compiler_directives={'language_level' : "3"})
     )
