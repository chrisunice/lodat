from setuptools import setup
from pip._internal.req import parse_requirements

# Get required packages for the project
required_packages = [str(req.requirement) for req in parse_requirements('./requirements.txt', session='')]

setup(
    name='lodat',
    version='1.0.0',
    author='Chris Unice',
    author_email='cunice@denmartech.com',
    packages=['lodat'],
    # scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/lodat/',
    # license='LICENSE.txt',
    description='LO Data Analysis Toolkit',
    long_description=open('README.md').read(),
    install_requires=required_packages,
)
