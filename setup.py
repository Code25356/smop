from setuptools import setup, find_packages

from smop.version import __version__ as __VERSION__

setup(
    author='Victor Leikehman',
    author_email='victorlei@gmail.com',
    description='Matlab to Python converter',
    license='MIT',
    keywords='convert translate matlab octave python',
    url='https://github.com/victorlei/smop',
    download_url='https://github.com/victorlei/smop',
    name='smop',
    version=__VERSION__,
    entry_points={'console_scripts': ['smop = smop.main:main', ], },
    packages=find_packages(),
    install_requires=['pytest', 'ply', 'numpy', 'scipy', 'networkx'],
    tests_require=['pytest'],
    test_suite='pytest',
)
