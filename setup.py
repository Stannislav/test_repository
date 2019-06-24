from setuptools import setup


NAME = 'my-package'
VERSION = '1.0'
DESCRIPTION = 'My test package with absolutely no content'
AUTHOR = 'Stanislav Schmidt'
PACKAGES = ['my_package']
URL = 'https://github.com/Stannislav/test_repository'

config = {
        'name': NAME,
        'version': VERSION,
        'description': DESCRIPTION,
        'author': AUTHOR,
        'packages': PACKAGES,
        'url': URL,
}

setup(**config)

