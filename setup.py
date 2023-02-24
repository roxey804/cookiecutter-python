import sys
from setuptools import setup, find_packages

requirements = [
    'pytest',
]

setup(
    name='{{project_name}}',
    version='{{version}}',
    packages=find_packages(),
    description='{{description}}',
    url='https://github.com/pelucid/{{project_name}}',
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest~=6.2.1', 'pytest-cov',],

    entry_points={
        'console_scripts': [
            ('deploy_client_facing_info='
             'gi_feature_definitions.console_scripts.deploy_client_facing_info:main'),
        ] #To be modified 
    },
    classifiers= ['Programming Language :: Python :: 3.9']
)
