import os

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'requirements.txt')) as f:
    INSTALL_REQUIRES = f.read().splitlines()


setup(
    name='eTaPR_pkg',
    description='',
    version='22.6.1',
    author='Won-Seok Hwang',
    author_email='hws0223@gmail.com',
    packages=['eTaPR_pkg'],
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': ['etapr=eTaPR_pkg.etapr:main'],
    }
)
