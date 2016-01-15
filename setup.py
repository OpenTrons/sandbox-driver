try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': "Python hardware drivers",
	'author': "OpenTrons",
	'url': 'http://opentrons.com',
	'version': '0.1',
	'install_requires': [
		'nose',
		'coverage',
		'pyserial'
	],
	'packages': ['gears'],
	'scripts': ['./bin/gears-hello'],
	'name': 'gears'
}

setup(**config)