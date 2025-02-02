from setuptools import find_packages, setup

setup(
name='studentperformanceindicator',
version='0.0.1',
author='Tasnimul',
author_email='tasnimuldatascience@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)