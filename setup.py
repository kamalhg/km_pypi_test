from distutils.core import setup
setup(
  name = 'km_pypi_test',
  packages = ['km_pypi_test'], # this must be the same as the name above
  version = '0.4',
  description = 'A random test lib',
  author = 'Kamal',
  author_email = 'kamalhg@gmail.com',
  url = 'https://github.com/kamalhg/km_pypi_test', # use the URL to the github repo
  download_url = 'https://github.com/kamalhg/km_pypi_test/tarball/0.3', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
  install_requires= [
    "pyyaml==3.11",
  ]
)