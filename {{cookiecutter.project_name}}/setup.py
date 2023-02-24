import sys
from setuptools import setup, find_packages

requirements = [
    'pytest',
]

setup(
    name='{{cookiecutter.project_name}}',
    version='{{cookiecutter.version}}',
    packages=find_packages(),
    description='{{cookiecutter.description}}',
    url='https://github.com/pelucid/{{cookiecutter.project_name}}',
    install_requires=requirements, # or can list packages directly here
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov',],

    entry_points={
        'console_scripts': [
            ('deploy_client_facing_info='
             'gi_feature_definitions.console_scripts.deploy_client_facing_info:main'),
        ] #To be modified 
    },
    classifiers= ['Programming Language :: Python :: 3.9']
)
