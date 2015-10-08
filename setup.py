try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='uw-usos-cli',
      version='0.0.1',
      author='teqwve',
      author_email='teqwve@openmailbox.org',
      description='commandline interface to University of Warsaw\'s USOS',
      url='https://github.com/teqwve/ucli',
      packages=('ucli',),
      entry_points={
          'console_scripts': [
              'ucli=ucli.main:main'
          ]
      })