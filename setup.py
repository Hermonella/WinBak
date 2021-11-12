from setuptools import setup

setup(name='WinBak',
      version='0.9',
      description='Script for automatically backup Windows.',
      url='https://github.com/Hermonella/WinBak',
      author='Hermonella',
      author_email='tovare13@gmail.com ',
    #   packages=['funniest'],
      install_requires=[
          'tkinter',
          'fnmatch',
          'tqdm',
          'wmi',
          'hurry.filesize',
      ],
      zip_safe=False)