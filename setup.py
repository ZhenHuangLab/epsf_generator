from setuptools import setup
from epsf_generator.__init__ import __author__, __email__, __version__

setup(
    name="epsf_generator",
    version=f'{__version__}',
    author=f'{__author__}',
    author_email=f'{__email__}',
    packages=["epsf_generator"],
    install_requires=[
        "numpy",
        "astropy==5.2.2",
        "photutils==1.5",
        "matplotlib==3.7.1"
    ],
    entry_points={
        "console_scripts": [
            "epsf_generator = epsf_generator.main:main"
        ]
    },
    license='BSD 3-Clause License',
    description='''A tiny script generating ePSF for deep sky image''',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=['epsf', 'astrophotography', 'psf'],
)
