from setuptools import setup


setup(name='reader-snap-diogo',


      version='0.1dev1',
      description='A test snap to read configuration into a TOML file',

      author='Muhammad Yahya & Felix Forster  - Diogo Carodoso',
      url='https://github.com/fdiogoc/snap-python.git',
      packages=['reader_main.writer_pkg', 'reader_main'],
      install_requires=['click', 'toml', ],

      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Utilities",
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Operating System :: POSIX :: Linux", ],

      entry_points={
          'console_scripts': [
              'reader-snap = reader.writer_main:init'
          ]
      },

      )