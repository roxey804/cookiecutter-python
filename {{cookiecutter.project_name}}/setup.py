import sys
from setuptools import setup, find_packages


setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.version}}',
    packages=find_packages(),
    description='{{cookiecutter.description}}',
    url='https://github.com/pelucid/{{cookiecutter.project_name}}',
    install_requires=[], # list packages  here
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov',],

    # entry_points={},
    
    classifiers= ['Programming Language :: Python :: {{cookiecutter.language_version}}']
)
