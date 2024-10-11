from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in healthcare_localization/__init__.py
from healthcare_localization import __version__ as version

setup(
	name='healthcare_localization',
	version=version,
	description='Doctypes and customizations for Healthcare Localization',
	author='Aryrosa Fuentes',
	author_email='aryrosa.fuentes@MENTUM.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
