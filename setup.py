from setuptools import setup, find_packages

setup(
    name='python-console-menu',
    version='0.1.0-indev',
    packages=find_packages(include='menu_functions'),
    author='DesertUo',
    description='A customizable command-line menu system for Python applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DesertUO/python-menu-system',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10', # The infamous 'match' statement
    tests_require=['pytest'],  # I just use the latest version of pytest
    test_suite='tests',  # Directory containing the tests
)